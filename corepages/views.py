from django.shortcuts import render
from home.models import sitedata
from product.models import Categories,Product
from django.core.paginator import Paginator
# Create your views here.


def about(request):
    return render(request, 'corepages/about.html')


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

def shop(request):
    products = Product.objects.all()
    productscount = products.count()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    categories = Categories.objects.all()
    site_data = sitedata.objects.all().last()
    context={
        'products': page_obj,
        'productscount': productscount,
        'categories': categories,
        'title': 'Shop',
        'site_data': site_data,
        }
    return render(request, 'home/shop.html',context)
