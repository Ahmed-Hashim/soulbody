# custom_users/urls.py
from django.urls import path
from .views import (
    password_change,
    register_user,
    activate,
    login_user,
    logout_user,
    save_profile,
    add_to_cart,
    view_cart,
    update_cart_item,
    remove_cart_item,
    checkout,
)
from .views import CustomPasswordResetView, CustomPasswordResetConfirmView


urlpatterns = [
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
    path("save_profile", save_profile, name="save_profile"),
    path("password_change", password_change, name="password_change"),
    path("register/", register_user, name="register_user"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path(
        "update_cart_item/",
        update_cart_item,
        name="update_cart_item",
    ),
    path("view_cart", view_cart, name="view_cart"),
    path(
        "remove_cart_item/<int:cart_item_id>/",
        remove_cart_item,
        name="remove_cart_item",
    ),
    path("checkout", checkout, name="checkout"),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # Add other URLs as needed
]
