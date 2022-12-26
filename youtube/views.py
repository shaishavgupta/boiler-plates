from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Video
from .serializers import VideoSerializer


class CustomPagination(PageNumberPagination):
    """Class for paginating the response"""

    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10


class GetVideos(generics.ListAPIView):
    """View for getting all the videos, order by latest published date."""

    serializer_class = VideoSerializer
    pagination_class = CustomPagination
    queryset = Video.objects.all().order_by('-publish_date_time')


class SearchVideos(generics.ListAPIView):

    serializer_class = VideoSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        title = self.request.query_params.get('title')
        description = self.request.query_params.get('description')
        title_qs, description_qs = Video.objects.none(), Video.objects.none()
        
        if title:
            title_qs = Video.objects.filter(title__contains=title)
        if description:
            description_qs = Video.objects.filter(description__contains=description)

        return (title_qs | description_qs).distinct().order_by('-publish_date_time')

        