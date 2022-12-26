from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from youtube.models import Video, ThumbNail, APIKey
from main.settings import YOUTUBE_API_VERSION, YOUTUBE_API_SERVICE_NAME


def search_youtube(query, max_results):
    """Fetching the latest videos for a search query using Youtube Data API.
    Args:
        query (str): search query.
        max_results(int): Maximum no of results we want in response from the
            Youtube Data API.
    Returns:
        results (list): List of all the videos data in dict format.
    """

    YOUTUBE_API_KEY = APIKey.objects.filter(source=YOUTUBE_API_SERVICE_NAME, is_valid=True).values_list('key',flat=True).first()
    if YOUTUBE_API_KEY is None:
        raise Exception(f'No API KEY for {YOUTUBE_API_SERVICE_NAME}')

    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)
        resp = youtube.search().list(q=query, part="id, snippet", maxResults=max_results).execute()
    except HttpError as e:
        if e.resp.status == 403 and e.error_details[0].get('reason')=='quotaExceeded':
            APIKey.objects.filter(key=YOUTUBE_API_KEY).update(is_valid=False)
            return search_youtube(query, max_results)

    return resp.get("items", [])


def get_date_time_from_string(date_time):
    """Create a datetime object from string of date and time.
    Args:
        date_time (str): String contains date and time.
    Return:
        obj: Returns a datetime object.
    """
    return datetime.strptime(
        date_time.split('T')[0] + ' ' + date_time.split('T')[1].split('Z')[0],
        '%Y-%m-%d %H:%M:%S')


def get_structured_video_data(result):
    """ Extract relevant values from Youtube Data API Results for video.
    Args:
        result (dict): Youtube Data API result in dictionary format.
    Returns:
        dict: Returns relevant values of result for video.
    """
    video_id = ''
    if 'videoId' in result['id']:
        video_id = result['id']['videoId']

    return {
        'video_id': video_id,
        'title': result["snippet"]["title"],
        'description': result['snippet']['description'],
        'channel_id': result['snippet']['channelId'],
        'publish_date_time': get_date_time_from_string(
            result['snippet']['publishedAt']),
    }


def get_structured_thumbnails_data(result, video):
    """ Extract relevant values from Youtube Data API Results
    for video thumbnails.
    Args:
        result (dict): Youtube Data API result in dictionary format.
    Returns:
        list: Returns relevant values of result for video thumbnails.
    """
    thumbnails = []
    for screen_size in result['snippet']['thumbnails']:
        width = result['snippet']['thumbnails'][screen_size].get('width')
        height = result['snippet']['thumbnails'][screen_size].get('height')
        url = result['snippet']['thumbnails'][screen_size]['url']
        thumbnails.append(ThumbNail(video=video, screen_size=screen_size, width=width, height=height, url=url))
    return thumbnails


def save_video_and_thumbail(result):
    """Save video and it's thumbnails in Database.
    Args:
        result (dict): Youtube Data API result in dictionary format.
    """
    video_dict = get_structured_video_data(result)
    video, created = Video.objects.get_or_create(**video_dict)

    if created:
        thumbnails = get_structured_thumbnails_data(result, video)
        ThumbNail.objects.bulk_create(thumbnails)


def search_and_add_youtube_videos():
    """function for fetching the latest videos
    and  storing it in database.
    """

    search_results = search_youtube('today news', 10)

    if search_results == {}:
        return

    for result in search_results:
        try:
            save_video_and_thumbail(result)
        except Exception as e:
            print(f"Exception {e} raised for data {result}")