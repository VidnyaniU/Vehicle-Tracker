from django.urls import re_path
from .consumers import VehicleTrackingConsumer

websocket_urlpatterns = [
    re_path(r'ws/tracking/', VehicleTrackingConsumer.as_asgi()),
]
