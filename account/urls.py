# custom_users/urls.py
from django.urls import path
<<<<<<< HEAD
from .views import register_user, activate,login_user,logout_user
=======
from .views import *
>>>>>>> 5f6b3bd7cc9c1efb4dfd3b1106962dccdba94f73

urlpatterns = [
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
]
