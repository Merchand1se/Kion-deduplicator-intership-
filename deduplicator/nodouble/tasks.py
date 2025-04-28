from celery import shared_task
from celery.app.log import logging
from django.utils import timezone

import redis

from .models import Event


#Настройка логирования
logger = logging.getLogger(__name__)

#Подключение Redis
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@shared_task()
def process_event(json_data, event_hash):

    """
    Обрабатывает входящие события
    Проверяет их уникальность через RedisBloom
    Сохраняет в БД уникальные события
    """

    if redis_client.execute_command("BF.EXISTS", "event_bloom", event_hash):
        logger.info("Event duplicate (Bloom)")
        return "Event duplicate"


    redis_client.execute_command("BF.ADD", "event_bloom", event_hash)

    Event.objects.create(event_name=json_data['event_name'], client_id=json_data['client_id'], product_id=json_data['product_id'], hash=event_hash)
    logger.info("Event created")
    return "Event created"