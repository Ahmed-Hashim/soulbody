# custom_users/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
]
