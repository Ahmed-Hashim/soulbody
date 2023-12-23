from django.shortcuts import render, redirect
from .forms import ClientUserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from product.models import Product, MedicalSystem, Categories
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
