import os

import isodate
from googleapiclient.discovery import build
import datetime


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlist_videos = youtube.playlists().list(part='snippet', id=playlist_id).execute()
        self.title = self.playlist_videos['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    def __str__(self):
        return f"{self.title}"

    @property
    def total_duration(self):
        '''Возвращает объект класса `datetime.timedelta` с суммарной длительность плейлиста'''
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                      part='contentDetails',
                                                      maxResults=50,
                                                      ).execute()

        video_ids = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        total_duration = datetime.timedelta()
        for video in video_response['items']:
            if 'duration' in video['contentDetails']:
                # YouTube video duration is in ISO 8601 format
                iso_8601_duration = video['contentDetails']['duration']
                duration = isodate.parse_duration(iso_8601_duration)
                total_duration += duration
        return total_duration

    def show_best_video(self):
        '''Возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)'''
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        current_video_likes = 0
        for video_id in video_ids:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id).execute()
            if int(video_response['items'][0]['statistics']['likeCount']) > current_video_likes:
                current_video_likes = int(video_response['items'][0]['statistics']['likeCount'])
            else:
                continue
        return f"https://youtu.be/{video_id}"
