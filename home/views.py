from django.shortcuts import render
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

    context = {'products': products,
               'systems': systems,
               'categories': categories,
               'sliders': sliders,
               'coldown': coldown,
               'tests': tests,
               'sitedata': site_data,

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

    context = {'products': products,
               'systems': systems,
               'categories': categories,
               'sliders': sliders,
               'coldown': coldown,
               'tests': tests,
               'sitedata': site_data,

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
    print(site_data)
    context = {
        'products': page_obj,
        'productscount': productscount,
        'categories': categories,
        'title': 'Shop',
        'sitedata': site_data,
    }
    return render(request, 'corepages/shop.html', context)
