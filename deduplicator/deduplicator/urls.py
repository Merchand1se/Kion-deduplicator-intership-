from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from api.views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/events/', permanent=False))
]