from django.shortcuts import render
from products.models import Product, MedicalSystem, Categories
from crm.models import Testimonials
from .models import *
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
    return render(request, "home/index.html", context)
