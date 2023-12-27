from django.urls import path
from . import views


urlpatterns = [
    path("show_cart/<int:id>", views.show_cart, name="show_cart"),
    path("show_product/<int:id>", views.show_product, name="show_product"),
]
