from rest_framework import serializers
from nodouble.models import Event
from django.utils import timezone


class EventSerializer(serializers.ModelSerializer):
    hash = serializers.CharField(read_only=True)

    class Meta:
        model = Event
        fields = ['client_id', 'event_name', 'product_id', 'hash']