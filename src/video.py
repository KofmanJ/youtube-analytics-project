import os
from googleapiclient.discovery import build

class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id).execute()
        self.url = f"https://www.youtube.com/watch?v={video_id}"
        self.title = video_response['items'][0]['snippet']['title']
        self.count_views = video_response['items'][0]['statistics']['viewCount']
        self.count_likes = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.pl_id = pl_id
