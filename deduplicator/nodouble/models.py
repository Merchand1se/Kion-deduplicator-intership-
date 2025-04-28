from django.db import models

class Event(models.Model):
    objects = models.Manager()

    client_id = models.CharField(max_length=255)
    event_name = models.CharField()
    product_id = models.CharField(max_length=255, default=1)
    hash = models.CharField(max_length=64, blank=True)
