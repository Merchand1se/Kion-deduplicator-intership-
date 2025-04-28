import redis
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Подключение к Redis (проверь, что host и port совпадают с docker-compose)
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

def initialize_bloom_filter():
    """
    Создаёт фильтр Блума в Redis, если он ещё не создан.
    Параметры:
    - 0.01 — вероятность ложного срабатывания (1%)
    - 1000000 — ожидаемое количество уникальных хэшей
    """
    try:
        redis_client.execute_command("BF.RESERVE", "event_bloom", 0.01, 1000000)
        logger.info("Bloom filter initialized")
    except redis.exceptions.ResponseError as e:
        if "exists" in str(e).lower():
            logger.info("Bloom filter already exists")
        else:
            logger.error(f"Error initializing Bloom filter: {e}")
            raise

if __name__ == "__main__":
    initialize_bloom_filter()
