import os
from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            api_key = os.getenv('API_KEY')
            youtube = build('youtube', 'v3', developerKey=api_key)
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id).execute()
            self.url = f"https://www.youtube.com/watch?v={video_id}"
            self.title = video_response['items'][0]['snippet']['title']
            self.count_views = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except:
            self.url = None
            self.title = None
            self.count_views = None
            self.like_count = None

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id
