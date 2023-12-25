from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ClientUserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from product.models import Product, MedicalSystem, Categories, Cart, CartItem
from home.models import sitedata
from .tokens import account_activation_token
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from .decorator import user_not_authenticated
from .forms import AddToCartForm, CartItemForm
import sweetify
from django.utils.translation import get_language
import json
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


@user_not_authenticated
def login_user(request):
    site_data = sitedata.objects.last()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()

    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Hello {user.email}! You have been logged in"
                )
                return redirect("home")
            else:
                messages.error(request, "Authentication failed. User is None.")
                print("Authentication failed. User is None.")
                # You can print more information about the authentication failure if needed
        else:
            messages.error(
                request, "Invalid form submission. Please correct the errors."
            )
            print("Form errors:", form.errors)
    form = UserLoginForm()

    context = {
        "categories": categories,
        "title": "Login",
        "form": form,
        "products": products,
        "systems": systems,
        "sitedata": site_data,
    }
    return render(request, "home/login.html", context)


@login_required
def logout_user(request):
    logout(request)
    return redirect("home")


@user_not_authenticated
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return redirect("login_user")
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect("home")


def activateEmail(request, user, to_email):
    site_email = "info@soulnbody.net"
    mail_subject = "Activate your user account."
    email_context = {
        "user": user,
        "domain": get_current_site(request).domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": account_activation_token.make_token(user),
        "protocol": "https" if request.is_secure() else "http",
    }
    acivation_email = get_template("email_activation.html")
    html_content = acivation_email.render(email_context)
    msg = EmailMultiAlternatives(
        mail_subject,
        html_content,
        site_email,
        [
            user.email,
        ],
    )
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        messages.success(
            request,
            f"Dear <b>{user.first_name}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.",
        )
    else:
        messages.error(
            request,
            f"Problem sending email to {to_email}, check if you typed it correctly.",
        )


@user_not_authenticated
def register_user(request):
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()
    form = ClientUserRegistrationForm(request.POST)
    if form.is_valid():
        client_user = form.save(commit=False)
        client_user.is_active = False
        client_user.set_password(
            form.cleaned_data.get("password")
        )  # Set the hashed password
        client_user.save()
        activateEmail(request, client_user, form.cleaned_data.get("email"))
        return redirect("home")

    context = {
        "form": form,
        "categories": categories,
        "title": "Login",
        "products": products,
        "systems": systems,
        "sitedata": site_data,
    }
    return render(request, "home/register.html", context)


def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def add_to_cart(request, product_id):
    lang = get_language()
    product = Product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product, defaults={"quantity": 1}
    )
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
    if lang == "en":
        return HttpResponse(
            status=204,
            headers={
                "HX-Trigger": json.dumps(
                    {
                        "close": "close",
                        "showMessage": "Product has been added to cart successfully",
                        "type": "bg-success",
                    }
                )
            },
        )

    else:
        return HttpResponse(
            status=204,
            headers={
                "HX-Trigger": json.dumps(
                    {
                        "close": "close",
                        "showMessage": "تم إضافة المنتج إلى العربة",
                        "type": "bg-success",
                    }
                )
            },
        )


def update_cart_item(request):
    if request.method == "POST":
        cart_items = json.loads(request.POST.get("cart_items", "[]"))

        # Process the cart items and update quantities
        updated_subtotals = {}
        for item in cart_items:
            cart_item = get_object_or_404(CartItem, id=item["id"])
            cart_item.quantity = item["quantity"]
            cart_item.save()
            updated_subtotals[item["id"]] = cart_item.calculate_subtotal()

        # Calculate new totals
        cart_subtotal = calculate_cart_subtotal(request.user)
        shipping_and_handling = calculate_shipping_and_handling()
        vat = calculate_vat(cart_subtotal)
        order_total = cart_subtotal + shipping_and_handling + vat

        return JsonResponse(
            {
                "updated_subtotals": updated_subtotals,
                "cart_subtotal": cart_subtotal,
                "shipping_and_handling": shipping_and_handling,
                "vat": vat,
                "order_total": order_total,
            }
        )

    return JsonResponse({"error": "Invalid request method"})


def remove_cart_item(request, cart_item_id):
    lang = get_language()
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    if lang == "en":
        return HttpResponse(
            status=204,
            headers={
                "HX-Trigger": json.dumps(
                    {
                        "close": "close",
                        "showMessage": "Product has been deleted",
                        "type": "bg-success",
                    }
                )
            },
        )

    else:
        return HttpResponse(
            status=204,
            headers={
                "HX-Trigger": json.dumps(
                    {
                        "close": "close",
                        "showMessage": "تم حذف المنتج من العربة",
                        "type": "bg-success",
                    }
                )
            },
        )


def calculate_cart_subtotal(user):
    # Replace this with your actual logic to fetch the user's cart items and calculate the subtotal
    cart_items = user.cart.cartitem_set.all()
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    return subtotal


def calculate_shipping_and_handling():
    # Replace this with your actual logic to calculate shipping and handling costs
    return Decimal("150.00")


def calculate_vat(cart_subtotal):
    # Replace this with your actual logic to calculate VAT
    return Decimal("0.14") * cart_subtotal


def view_cart(request):
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()
    cart = Cart.objects.get(user=request.user)
    cart_subtotal = calculate_cart_subtotal(request.user)
    shipping_and_handling = calculate_shipping_and_handling()
    vat = calculate_vat(cart_subtotal)
    order_total = cart_subtotal + shipping_and_handling + vat
    form = CartItemForm
    context = {
        "cart_subtotal": cart_subtotal,
        "shipping_and_handling": shipping_and_handling,
        "vat": vat,
        "order_total": order_total,
        "cart": cart,
        "form": form,
        "categories": categories,
        "title": "Login",
        "products": products,
        "systems": systems,
        "sitedata": site_data,
    }
    cart = Cart.objects.get(user=request.user)
    form = CartItemForm

    return render(request, "home/view_cart.html", context)


@login_required
def checkout(request):
    user_email = request.user.email

    cart_items = Cart.objects.get(user=request.user).cartitem_set.all()
    cart_subtotal = calculate_cart_subtotal(request.user)
    shipping_and_handling = calculate_shipping_and_handling()
    vat = calculate_vat(cart_subtotal)
    order_total = cart_subtotal + shipping_and_handling + vat
    # Send admin notification email
    admin_subject = "New Order Received"
    admin_message = render_to_string(
        "admin_notification_email.html",
        {"cart_items": cart_items, "order_total": order_total},
    )
    send_mail(
        admin_subject, admin_message, "info@soulnbody.net", ["info@soulnbody.net"]
    )

    # Send user confirmation email
    user_subject = "Order Confirmation"
    user_message = render_to_string(
        "user_confirmation_email.html",
        {"cart_items": cart_items, "order_total": order_total},
    )
    send_mail(user_subject, user_message, "info@soulnbody.net", [user_email])

    # Additional logic for order confirmation, payment processing, etc.
    lang = get_language()
    if lang == "en":
        sweetify.success(
            request,
            "We received your request Successfully ",
            text=f"Thank you {request.user.username} for choosing us!",
            button="Ok",
            timer=5000,
        )
        return redirect("home")
    else:
        sweetify.success(
            request,
            "طلب ناجح",
            text=f"شكراً {request.user.username} لإختيارك لنا!",
            timer=5000,
        )
        return redirect("home")
