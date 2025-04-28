import json
import hashlib

from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import EventSerializer
from nodouble.models import Event
from nodouble.tasks import process_event



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)




        # Хешируем входной JSON
        json_data = serializer.validated_data
        json_str = json.dumps(json_data, sort_keys=True).encode("utf-8")
        event_hash = hashlib.sha256(json_str).hexdigest()


        # Отправка задачи в очередь — без сохранения в базу на этом этапе
        result = process_event.delay(json_data, event_hash)
        response = result.get()  # Получаем результат выполнения

        return Response({'data': response, "status": result.status})
