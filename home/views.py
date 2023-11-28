from django.shortcuts import render
from products.models import Product,MedicalSystem,Categories
from .models import *
# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems=MedicalSystem.objects.all()
    sliders = MainSlider.objects.filter(active=True)
    coldown=Cooldown.objects.filter(active=True).last()

    context={'products':products,
             'systems':systems,
             'categories':categories,
             'sliders':sliders,
             'coldown':coldown,

             }
    return render(request , "home/index.html",context)