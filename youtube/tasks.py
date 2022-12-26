from celery import shared_task
from youtube.utils import search_and_add_youtube_videos


@shared_task(bind=True)
def search_youtube_videos(self):
    """Asynchronous Service for searching and adding youtube videos."""
    print(f"Inside the search_youtube_videos function {self}")
    search_and_add_youtube_videos()