from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import sitedata
from product.models import *


def show_product(request, id):
    product_details = get_object_or_404(Product, id=id)
    context = {
        "product_details": product_details,
    }
    return render(request, "home/modals/showproduct.html", context)


def show_cart(request, id):
    cart_details = get_object_or_404(Cart, id=id)
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()
    context = {
        "categories": categories,
        "title": "Request Clinic",
        "products": products,
        "systems": systems,
        "sitedata": site_data,
        "cart": cart_details,
    }
    return render(request, "home/modals/show_cart.html", context)
