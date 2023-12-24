# custom_users/urls.py
from django.urls import path
from .views import (
    register_user,
    activate,
    login_user,
    logout_user,
    add_to_cart,
    view_cart,
    update_cart_item,
    remove_cart_item,
)

urlpatterns = [
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path(
        "update_cart_item/<int:cart_item_id>/",
        update_cart_item,
        name="update_cart_item",
    ),
    path("cart/", view_cart, name="cart"),
    path(
        "remove_cart_item/<int:cart_item_id>/",
        remove_cart_item,
        name="remove_cart_item",
    ),
    # Add other URLs as needed
]
