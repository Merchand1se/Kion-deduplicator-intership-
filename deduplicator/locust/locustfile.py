from locust import HttpUser, task, between
from datetime import datetime

import random


class Event(HttpUser):
    wait_time = between(0, 0) #Без задержки для достижения 500RPS

    @task
    def send_event(self):
        num = random.randint(1, 10000)

        payload = {
            "client_id" : num,
            "event_name" : f"event-{num}",
            "product_id" : num,
        }

        headers = {"Content-Type" : "application/json"}
        self.client.post("/api/events/", json=payload, headers=headers)