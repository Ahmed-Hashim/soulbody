from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ClientUserRegistrationForm, PasswordChangingForm, ProfileForm
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

from django.contrib.auth import update_session_auth_hash


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
    lang = get_language()
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        if lang == "en":
            messages.success(
                request,
                "Thank you for your email confirmation. Now you can login your account.",
            )
        else:
            messages.success(
                request,
                "شكرًا لتأكيدك عبر البريد الإلكتروني. يمكنك الآن تسجيل الدخول إلى حسابك.",
            )
        return redirect("login_user")
    else:
        if lang == "en":
            messages.error(request, "Activation link is invalid!")
        else:
            messages.error(request, "الرابط التفعيل غير صالح!")

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
    product = get_object_or_404(Product, pk=product_id)

    # Get the last not completed cart for the user
    last_not_completed_cart = Cart.objects.filter(
        user=request.user, completed=False
    ).first()

    if not last_not_completed_cart:
        # If there is no not completed cart, create a new one
        last_not_completed_cart = Cart.objects.create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=last_not_completed_cart, product=product, defaults={"quantity": 1}
    )

    if not created:  # If the item already exists, increment the quantity
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
        cart_subtotal = round(calculate_cart_subtotal(request.user))
        shipping_and_handling = round(calculate_shipping_and_handling())
        vat = round(calculate_vat(cart_subtotal))
        order_total = round(cart_subtotal + shipping_and_handling + vat)

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
    # Get the last incomplete cart for the user
    last_incomplete_cart = (
        Cart.objects.filter(user=user, completed=False).order_by("-created_at").first()
    )

    if last_incomplete_cart:
        # Retrieve cart items from the last incomplete cart
        cart_items = last_incomplete_cart.cartitem_set.all()

        # Calculate the subtotal
        subtotal = sum(item.product.price * item.quantity for item in cart_items)
        return subtotal
    else:
        # If no incomplete cart is found, return 0 as the subtotal
        return 0


def calculate_shipping_and_handling():
    # Replace this with your actual logic to calculate shipping and handling costs
    return Decimal("150")


def calculate_vat(cart_subtotal):
    # Replace this with your actual logic to calculate VAT
    return Decimal("0.14") * cart_subtotal


def view_cart(request):
    site_data = sitedata.objects.all().last()
    categories = Categories.objects.all()
    systems = MedicalSystem.objects.all()
    products = Product.objects.all()
    cart = (
        Cart.objects.filter(user=request.user, completed=False)
        .order_by("-created_at")
        .first()
    )
    cart_subtotal = round(calculate_cart_subtotal(request.user))
    shipping_and_handling = round(calculate_shipping_and_handling())
    vat = round(calculate_vat(cart_subtotal))
    order_total = round(cart_subtotal + shipping_and_handling + vat)
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
    return render(request, "home/view_cart.html", context)


@login_required
def checkout(request):
    # Get the user's active cart (not completed)
    active_cart = Cart.objects.filter(user=request.user, completed=False).first()

    if active_cart and not active_cart.completed:
        # Retrieve cart items from the completed cart
        cart_items = active_cart.cartitem_set.all()

        # Perform your calculations for the new cart
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
        user_email = request.user.email
        user_subject = "Order Confirmation"
        user_message = render_to_string(
            "user_confirmation_email.html",
            {"cart_items": cart_items, "order_total": order_total},
        )
        send_mail(user_subject, user_message, "info@soulnbody.net", [user_email])

        # Mark the current active cart as completed
        active_cart.completed = True
        active_cart.save()
    else:
        print("No active or completed cart found for the user.")

    # Create a new cart for the user only if no active or completed cart is found
    try:
        if not active_cart or active_cart.completed:
            new_cart = Cart.objects.create(user=request.user, completed=False)
            print("New cart created")
    except Exception as e:
        print(f"Error creating new cart: {e}")

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


def save_profile(request):
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if profile_form.is_valid():
        profile_form.save()
        lang = get_language()
        if lang == "en":
            sweetify.success(
                request,
                "Success request",
                button="Ok",
                timer=5000,
            )
            return redirect("user_account")
        else:
            sweetify.success(
                request,
                "طلب ناجح",
                timer=5000,
            )
            return redirect("user_account")
    return redirect("user_account")


def password_change(request):
    lang = get_language()
    if request.method == "POST":
        password_form = PasswordChangingForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)

            if lang == "en":
                sweetify.success(
                    request,
                    "Success request",
                    button="Ok",
                    timer=5000,
                )
                return redirect("user_account")
            else:
                sweetify.success(
                    request,
                    "طلب ناجح",
                    timer=5000,
                )
                return redirect("user_account")
        else:
            if lang == "en":
                sweetify.error(
                    request,
                    "Enter right data",
                    button="Ok",
                    timer=5000,
                )
                return redirect("user_account")
            else:
                sweetify.error(
                    request,
                    "ادخل معلومات صحيحة",
                    timer=5000,
                )
                return redirect("user_account")

    else:
        password_form = PasswordChangingForm(request.user)

    return redirect("user_account", {"password_form": password_form})
