# Django's imports
from django.urls import path

# Developer's imports
from .views import index, channel


urlpatterns = [
    path("", index, name="index"),
    path("channel/<int:pk>", channel, name="channel"),
]
