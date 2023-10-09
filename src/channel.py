import json
import os
from googleapiclient.discovery import build
# import isodate

# api_key: str = os.getenv('API_KEY')
# print(os.getenv('API_KEY'))

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel = channel['items'][0]
        self.title = channel['snippet']['title']
        self.description = channel['snippet']['description']
        self.url = f"https://www.youtube.com/{channel['snippet']['customUrl']}"
        self.count_subscribers = int(channel['statistics']['subscriberCount'])
        self.video_count = int(channel['statistics']['videoCount'])
        self.count_views = int(channel['statistics']['viewCount'])

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """
        Возвращает общее количество подписчиков
        """
        return self.count_subscribers + other.count_subscribers

    def __sub__(self, other):
        """
        Возвращает вычтенное количество подписчиков
        """
        return self.count_subscribers - other.count_subscribers

    def __gt__(self, other):
        """
        Сравнивают количество подписчиков
        """
        return self.count_subscribers > other.count_subscribers

    def __ge__(self, other):
        """
        Сравнивают количество подписчиков
        """
        return self.count_subscribers >= other.count_subscribers

    def __lt__(self, other):
        """
        Сравнивают количество подписчиков
        """
        return self.count_subscribers < other.count_subscribers

    def __le__(self, other):
        """
        Сравнивают количество подписчиков
        """
        return self.count_subscribers <= other.count_subscribers

    def __eq__(self, other):
        """
        Сравнивают количество подписчиков
        """
        return self.count_subscribers == other.count_subscribers

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = (youtube.channels().list(id=self.channel_id, part='snippet,statistics')).execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, file_name):
        """
        Вставляет данные в файл формата json
        """
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.count_subscribers,
            "video_count": self.video_count,
            "view_count": self.count_views
        }
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)


