from django.urls import re_path

from . import consumers
from django.urls import  re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/data/$', consumers.DataConsumer.as_asgi()),
]
