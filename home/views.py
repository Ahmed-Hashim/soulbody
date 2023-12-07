from django.shortcuts import render
from home.forms import Contact_form
from product.models import Product, MedicalSystem, Categories
from crmsb.models import Customer, Testimonials
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
    context = {}
    return render(request, "home/base.html", context)


def shop(request):
    products = Product.objects.all()
    systems = MedicalSystem.objects.all()
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
        "systems": systems,
        "title": "Shop",
        "sitedata": site_data,
    }
    return render(request, "corepages/shop.html", context)


def product_details(request, id):
    products = Product.objects.all()
    product = products.filter(id=id)[0]
    systems = MedicalSystem.objects.all()
    categories = Categories.objects.all()
    site_data = sitedata.objects.all().last()
    context = {
        "products": products,
        "product": product,
        "categories": categories,
        "systems": systems,
        "title": "Shop",
        "sitedata": site_data,
    }
    return render(request, "corepages/product_details.html", context)


def category_products(request, id):
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    category = categories.filter(id=id)[0]
    products = Product.objects.filter(category=id)
    site_data = sitedata.objects.all().last()
    context = {
        "products": products,
        "productscount": products.count(),
        "categories": categories,
        "systems": systems,
        "category_n": category,
        "title": "Shop",
        "sitedata": site_data,
    }
    return render(request, "corepages/shop.html", context)


def contact_us(request):
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    form = Contact_form()
    if request.method == "POST":
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()

    site_data = sitedata.objects.all().last()
    context = {
        "form": form,
        "categories": categories,
        "systems": systems,
        "title": "Contact Us",
        "sitedata": site_data,
    }

    return render(request, "corepages/contact_us.html", context)


def about_us(request):
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    tests = Testimonials.objects.filter(active=True)
    coldown = Cooldown.objects.filter(active=True).last()
    expert_doctors = Customer.objects.filter(expert=True)
    fqas = FQA_About.objects.all()
    context = {
        "categories": categories,
        "title": "About Us",
        "coldown": coldown,
        "systems": systems,
        "tests": tests,
        "fqas": fqas,
        "expert_doctors": expert_doctors,
        "sitedata": site_data,
    }
    return render(request, "corepages/about.html", context)


def medical_systems(request, id):
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    medical_systems = MedicalSystem.objects.get(id=id)
    system_tags = MedicalSystem.objects.prefetch_related("tags").all()
    products = Product.objects.all()
    context = {
        "categories": categories,
        "title": "About Us",
        "products": products,
        "medical_systems": medical_systems,
        "system_tags": system_tags,
        "sitedata": site_data,
    }
    return render(request, "corepages/systems_details.html", context)
