from django.urls import path
from .views import GetVideos, SearchVideos





urlpatterns = [
	path('get_videos/', GetVideos.as_view()),
	path('search/', SearchVideos.as_view()),
]