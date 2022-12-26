from rest_framework import serializers

from .models import Video, ThumbNail
# from .utils import 

class VideoSerializer(serializers.ModelSerializer):
    """Serializer for Video Model."""
    thumbnails = serializers.SerializerMethodField()

    def get_thumbnails(self, obj):
        """
        Returns all thumbnails of the video.
        """
        return ThumbNailSerializer(ThumbNail.objects.filter(video_id=obj.id), many=True).data

    class Meta:
        model = Video
        fields = '__all__'


class ThumbNailSerializer(serializers.ModelSerializer):
    """Serializer for VideoThumbNail Model."""
    class Meta:
        model = ThumbNail
        fields = '__all__'