from django.urls import path
from . import views


urlpatterns = [
    path("shop", views.shop, name="shop"),
    path("product_details/<int:id>", views.product_details, name="product_details"),
    path(
        "category_products/<int:id>", views.category_products, name="category_products"
    ),
    path("medical_systems/<int:id>", views.medical_systems, name="medical_systems"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("about_us", views.about_us, name="about_us"),
    path("request_clinic/<int:id>", views.request_clinic, name="request_clinic"),
    
]
