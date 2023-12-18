# custom_users/urls.py
from django.urls import path
from .views import register_user,activate

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    # Add other URLs as needed
]
