from django.shortcuts import redirect, render
from account.forms import CartItemForm, ProfileForm, PasswordChangingForm
from home.forms import Contact_form, Request_Clinic_form, Request_Hosbital_form
from product.models import Product, MedicalSystem, Categories, Cart, CartItem
from crmsb.models import Customer, Testimonials
from .models import *
from django.core.paginator import Paginator
import sweetify
from django.utils.translation import get_language
from django.http import JsonResponse, HttpResponse


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

    if request.user.is_authenticated:
        # Try to get the user's active cart (not completed)
        active_cart = Cart.objects.filter(user=request.user, completed=False).first()
        context.update({"cart": active_cart})

    return render(request, "home/home.html", context)


def terms_conditions(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sitedata": site_data,
    }

    if request.user.is_authenticated:
        # Try to get the user's active cart (not completed)
        active_cart = Cart.objects.filter(user=request.user, completed=False).first()
        context.update({"cart": active_cart})

    return render(request, "corepages/terms_conditions.html", context)


def claim(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sitedata": site_data,
    }

    if request.user.is_authenticated:
        # Try to get the user's active cart (not completed)
        active_cart = Cart.objects.filter(user=request.user, completed=False).first()
        context.update({"cart": active_cart})

    return render(request, "corepages/claim.html", context)


def privacy_policy(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sitedata": site_data,
    }

    if request.user.is_authenticated:
        # Try to get the user's active cart (not completed)
        active_cart = Cart.objects.filter(user=request.user, completed=False).first()
        context.update({"cart": active_cart})

    return render(request, "corepages/privacy_policy.html", context)


def base(request):
    context = {}
    return render(request, "home/base.html", context)


def custom_404(request, exception):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sitedata": site_data,
    }

    return render(
        request,
        "errorpages/error_404.html",
        context,
        status=404,
    )


def custom_500(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    site_data = sitedata.objects.all().last()

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sitedata": site_data,
    }
    return render(
        request,
        "errorpages/error_500.html",
        context,
        status=500,
    )


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
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()
    if "Clinic" in medical_systems.en_name:
        form = Request_Clinic_form()
        lang = get_language()
        if request.method == "POST":
            form = Request_Clinic_form(request.POST)

            if form.is_valid():
                name = form.cleaned_data["name"]
                form.save()
                if lang == "en":
                    sweetify.success(
                        request,
                        "We received your request Successfully ",
                        text=f"Thank you {name} for choosing us!",
                        button="Ok",
                        timer=5000,
                    )
                    return redirect("home")
                else:
                    sweetify.success(
                        request,
                        "طلب ناجح",
                        text=f"شكراً {name} لإختيارك لنا!",
                        timer=5000,
                    )
                    return redirect("home")
    elif "Hospital" in medical_systems.en_name:
        form = Request_Hosbital_form()
        lang = get_language()
        if request.method == "POST":
            form = Request_Hosbital_form(request.POST)
            if form.is_valid():
                form.save()
                if lang == "en":
                    sweetify.success(
                        request,
                        "We received your request Successfully ",
                        text=f"Thank you {name} for choosing us!",
                        button="Ok",
                        timer=5000,
                    )
                    return redirect("home")
                else:
                    sweetify.success(
                        request,
                        "طلب ناجح",
                        text=f"شكراً {name} لإختيارك لنا!",
                        timer=5000,
                    )
                    return redirect("home")

    context = {
        "categories": categories,
        "title": "Medical Systems",
        "products": products,
        "systems": systems,
        "medical_systems": medical_systems,
        "sitedata": site_data,
        "form": form,
    }
    return render(request, "corepages/systems_details.html", context)


def request_clinic(request, id):
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    medical_systems = MedicalSystem.objects.get(id=id)
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()

    context = {
        "categories": categories,
        "title": "Request Clinic",
        "products": products,
        "systems": systems,
        "medical_systems": medical_systems,
        "sitedata": site_data,
    }
    return render(request, "corepages/request_clinic.html", context)


def user_account(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    site_data = sitedata.objects.all().last()
    completed_carts = Cart.objects.filter(user=request.user, completed=True)
    profile_form = ProfileForm(instance=request.user.profile)
    password_form = PasswordChangingForm(user=request.user)
    cart_subtotals = []
    for completed_cart in completed_carts:
        cart_items = completed_cart.cartitem_set.all()
        subtotal = sum(item.calculate_subtotal() for item in cart_items)
        cart_subtotals.append({"cart": completed_cart, "subtotal": subtotal})

    context = {
        "products": products,
        "systems": systems,
        "categories": categories,
        "sitedata": site_data,
        "carts": completed_carts,
        "profile_form": profile_form,
        "password_form": password_form,
        "completed_carts": cart_subtotals,
    }

    if request.user.is_authenticated:
        # Try to get the user's active cart (not completed)
        active_cart = Cart.objects.filter(user=request.user, completed=False).first()
        context.update({"cart": active_cart})

    return render(request, "home/my_account.html", context)
