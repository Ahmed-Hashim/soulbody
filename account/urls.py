# custom_users/urls.py
from django.urls import path
from .views import register_user, activate,login_user,logout_user

urlpatterns = [
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    # Add other URLs as needed
]
