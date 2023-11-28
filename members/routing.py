from django.urls import path
from project.consumer import NotificationConsumer
from members.consumer import PersonalChatConsumer,OnlineStatusConsumer


websocket_urlpatterns = [
    path("ws/notifications/", NotificationConsumer.as_asgi()),
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
    path('ws/status/', OnlineStatusConsumer.as_asgi()),

]
