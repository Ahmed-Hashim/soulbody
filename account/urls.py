# custom_users/urls.py
from django.urls import path
from .views import register_user, activate, login_user, logout_user,add_to_cart,view_cart

urlpatterns = [
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="cart"),
    # Add other URLs as needed
]
