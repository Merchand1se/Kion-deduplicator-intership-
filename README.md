# Продуктовый Дедупликатор Событий (Event Deduplicator)

Микросервис для обнаружения и обработки дубликатов событий в продуктовой аналитике. Поддерживает различные стратегии дедупликации и интеграцию с RabbitMQ.

## 🔍 Особенности

- Обнаружение дубликатов по event_id, product_id и event_name
- Поддержка Redis и PostgreSQL для хранения состояния
- Асинхронная обработка событий через Celery/RQ
- Тестирование с locust при нагрузке 500RPS
- REST API для ручного управления

## 🛠 Технологический стек

- Python 3.10+
- Django/DRF (Http интерфейс)
- Redis/PostgreSQL (хранилище состояний)
- Celery/RabbitMQ (источник событий)
- Docker (оркестрация)

### Установка

python -m venv venv
source venv/bin/activate
docker-compose up -d --build

-Для запуска достаточно запустить docker-compose, он установит requirements.txt, примении миграции, запустит сервер и инициализирует фильтр Блума в Redis.



