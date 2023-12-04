from django.shortcuts import render
from home.models import sitedata
from product.models import Categories, Product
from django.core.paginator import Paginator
# Create your views here.



def claim(request):
    return render(request, 'corepages/claim.html')


def contact_us(request):
    return render(request, 'corepages/contact_us.html')


def fqa(request):
    return render(request, 'corepages/fqa.html')


def medical_tourism(request):
    return render(request, 'corepages/medical_tourism.html')


def privacy_policy(request):
    return render(request, 'corepages/privacy_policy.html')


def terms_conditions(request):
    return render(request, 'corepages/terms_conditions.html')



