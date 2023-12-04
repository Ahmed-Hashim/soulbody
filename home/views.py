from django.shortcuts import render
from home.forms import Contact_form
from product.models import Product, MedicalSystem, Categories
from crmsb.models import Testimonials
from .models import *
import random
from django.core.paginator import Paginator

# Assuming products is a queryset

# Create your views here.


def home(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    sliders = MainSlider.objects.filter(active=True)
    tests = Testimonials.objects.filter(active=True)
    coldown = Cooldown.objects.filter(active=True).last()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sliders": sliders,
        "coldown": coldown,
        "tests": tests,
        "sitedata": site_data,
    }
    return render(request, "home/home.html", context)


def base(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    sliders = MainSlider.objects.filter(active=True)
    tests = Testimonials.objects.filter(active=True)
    coldown = Cooldown.objects.filter(active=True).last()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sliders": sliders,
        "coldown": coldown,
        "tests": tests,
        "sitedata": site_data,
    }
    return render(request, "home/base.html", context)


def shop(request):
    products = Product.objects.all()
    productscount = products.count()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    categories = Categories.objects.all()
    site_data = sitedata.objects.all().last()
    context = {
        "products": page_obj,
        "productscount": productscount,
        "categories": categories,
        "title": "Shop",
        "sitedata": site_data,
    }
    return render(request, "corepages/shop.html", context)


def product_details(request, id):
    products = Product.objects.all()
    product = products.filter(id=id)[0]

    categories = Categories.objects.all()
    site_data = sitedata.objects.all().last()
    context = {
        "products": products,
        "product": product,
        "categories": categories,
        "title": "Shop",
        "sitedata": site_data,
    }
    return render(request, "corepages/product_details.html", context)


def category_products(request, id):
    categories = Categories.objects.all()
    category = categories.filter(id=id)[0]
    products = Product.objects.filter(category=id)
    site_data = sitedata.objects.all().last()
    context = {
        "products": products,
        "productscount": products.count(),
        "categories": categories,
        "category_n": category,
        "title": "Shop",
        "sitedata": site_data,
    }
    return render(request, "corepages/shop.html", context)


def contact_us(request):
    form = Contact_form()

    if request.method == "POST":
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()

    site_data = sitedata.objects.all().last()
    context = {
        "form": form,
        "title": "Contact Us",
        "sitedata": site_data,
    }

    return render(request, "corepages/contact_us.html", context)


def about_us(request):
    site_data = sitedata.objects.all().last()
    context = {
        "title": "About Us",
        "sitedata": site_data,
    }
    return render(request, "corepages/about.html", context)
