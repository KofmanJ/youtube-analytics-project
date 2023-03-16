# Режимы доступа. Домашнее задание

## Описание задачи
Модифицируйте конструктор `Channel`, чтобы после инициализации экземпляр имел следующие атрибуты, заполненные реальными данными канала:
- id канала
- название канала
- описание канала
- ссылка на канал
- количество подписчиков
- количество видео
- общее количество просмотров

Добавьте в класс `Channel` следующие методы:
- класс-метод `get_service()`, возвращающий объект для работы с YouTube API
- метод `to_json()`, сохраняющий в файл значения атрибутов экземпляра `Channel`

## Ожидаемое поведение
- Код в файле `main.py` должен выдавать ожидаемые значения