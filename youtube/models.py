from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Video(TimeStampedModel):
    title =  models.TextField(null=False, blank=False)
    description =  models.TextField(null=False, blank=False)
    publish_date_time =  models.DateTimeField(null=False, blank=False, auto_now=False)
    video_id = models.TextField(unique=True)
    channel_id = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'videos'

    def __str__(self):
        return self.title


class ThumbNail(TimeStampedModel):
    DEFAULT='default'
    MEDIUM='medium'
    HIGH='high'

    SCREEN_SIZE_CHOICES = (
        (DEFAULT, DEFAULT),
        (MEDIUM, MEDIUM),
        (HIGH, HIGH),
    )
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="thumbnail")
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    screen_size = models.CharField(null=False, blank=False, max_length=20, choices=SCREEN_SIZE_CHOICES)
    url = models.TextField()

    class Meta:
        db_table = 'thumbnails'
        unique_together = ('screen_size', 'url')

    def __str__(self):
        return f"{self.video.title}-{self.screen_size}-{self.url}"


class APIKey(TimeStampedModel):
    YOUTUBE = 'youtube'
    SOURCE_CHOICES = (
        (YOUTUBE, YOUTUBE),
    )
    source = models.CharField(max_length=20, null=False, blank=False, choices=SOURCE_CHOICES)
    key = models.TextField(unique=True, null=False, blank=False)
    is_valid = models.BooleanField(default=True)

    class Meta:
        db_table = 'api_keys'
    
    def __str__(self):
        return f"{self.source}-{self.key}-{self.is_valid}"