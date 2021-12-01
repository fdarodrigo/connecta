# Developer's imports
from django.urls import path

# View's imports
from .views import (
    SignUpView,
    index,
)

urlpatterns = [
    # View to subscribe new users
    path("signup/", SignUpView.as_view(), name="signup"),
    path("index/", index, name="index"),
]
