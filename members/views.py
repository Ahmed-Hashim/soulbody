# from ipware import get_client_ip
# import requests
from .models import AppDownLoad, Profile, Chat, Messege
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from members.models import Profile
from .forms import ImageChageForm, ProfileForm, UserUpdateForm, PasswordChangingForm
from django.contrib.auth.decorators import login_required
import os
import environ
from django.http import HttpResponseRedirect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("settings")
    success_message = "Your password has been changed."
    title = "Change Password"


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome")
            return redirect("dashboard")
        else:
            return redirect("login")
    return render(request, "login.html")


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out..")
    return redirect("login")


@login_required
def profile(request):
    profile = request.user.profile
    context = {
        "profile": profile,
    }
    form = ProfileForm(instance=profile)
    if request.method == "POST" and "profileUpdate" in request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

        return redirect("profile")
    context = {
        "update_profile": profile,
        "form": form,
        "profile": profile,
        "title": "Profile",
    }
    return render(request, "registration/profile.html", context)


@login_required
def settings(request):
    user = request.user

    context = {
        "profile": user,
    }
    form = UserUpdateForm(instance=request.user)

    if request.method == "POST" and "profile_data" in request.POST:
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

        return redirect("settings")
    context = {
        "settings": settings,
        "form": form,
        "title": "Settings",
    }
    return render(request, "registration/settings.html", context)


@login_required
def changeProfileImage(request):
    form = ImageChageForm(request.POST, request.FILES,
                          instance=request.user.profile)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return JsonResponse({"close": True})
        else:
            print("Form is not valid")

    context = {"forma": form}
    return render(request, "registration/partial/changePhoto.html", context)


@login_required
def users(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {"profiles": profiles}
    return render(request, "registration/users_list.html", context)


@login_required
def chat(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        "profiles": profiles,
        "title": "Messanger",
    }
    return render(request, "chat/messenger.html", context)


@login_required
def mainchat(request, id):
    user_admin = request.user.profile
    user2 = Profile.objects.get(id=id)
    chat = Chat.objects.get(id=get_or_create_chat(user_admin.id, id))
    messages = Messege.objects.filter(chat=chat).order_by('timestamp')

    context = {

        "user_admin": user_admin,
        "user2": user2,
        "messages": messages,  # Pass the chat messages to the template
    }
    return render(request, "chat/mainchat.html", context)


def get_group_name(user1, user2):
    my_id = user1
    other_user_id = user2
    if int(other_user_id) > int(my_id):
        room_name = f'{my_id}-{other_user_id}'
    else:
        room_name = f'{other_user_id}-{my_id}'

    room_group_name = 'chat_%s' % room_name
    return room_group_name


def get_or_create_chat(user1, user2):
    # Get the user profiles based on their IDs
    user1 = Profile.objects.get(id=user1)
    user2 = Profile.objects.get(id=user2)
    # Check if a chat exists between user1 and user2 in both directions
    chat1 = Chat.objects.filter(user1=user1, user2=user2).first()
    chat2 = Chat.objects.filter(user1=user2, user2=user1).first()
    if chat1:
        # If a chat exists, redirect to that chat's page or do whatever you want
        return chat1.id
    elif chat2:
        # If a chat exists in the opposite direction, redirect to that chat's page or do whatever you want
        return chat2 .id
    else:
        # If no chat exists, create a new chat and redirect to it
        if int(user2.id) > int(user1.id):
            new_chat = Chat.objects.create(user1=user2, user2=user1)
            return new_chat.id
        else:
            new_chat = Chat.objects.create(user1=user1, user2=user2)
            return new_chat.id


def download_app(request):
    client_ip = request.META.get("HTTP_X_FORWARDED_FOR")
    if client_ip is not None:
        ip = client_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    parsed_agent = httpagentparser.detect(user_agent)
    # Check if it's an iPhone
    if 'iPhone' in user_agent:
        device_type = 'iPhone'
        try:
            try:
                response = DbIpCity.get(ip, api_key='free')
            except:
                response = {"city": "NotExist",
                            "country": "NotExist", "regoin": "NotExist"}
            AppDownLoad.objects.create(
                device_ip=ip, city=response.city, country=response.country, regoin=response.region, deviceType=device_type)
        except:
            print("Already Exsit")

        # print(user_agent)
        return HttpResponseRedirect(env("IOS_URL"))
    # Check if it's an Android device
    elif 'Android' in user_agent:
        device_type = 'Android'
        try:
            try:
                response = DbIpCity.get(ip, api_key='free')
            except:
                response = {"city": "NotExist",
                            "country": "NotExist", "regoin": "NotExist"}
            AppDownLoad.objects.create(
                device_ip=ip, city=response.city, country=response.country, regoin=response.region, deviceType=device_type)
        except:
            pass
        # print(user_agent)
        return HttpResponseRedirect(env("ANDRIOD_URL"))
    else:
        if parsed_agent.get('os', '')["name"] :
            device_type = parsed_agent.get('os', '')["name"]
        else :
            device_type = "UnKnown"
        try:
            try:
                response = DbIpCity.get(ip, api_key='free')
            except:
                response = {"city": "NotExist",
                            "country": "NotExist", "regoin": "NotExist"}
            AppDownLoad.objects.create(
                device_ip=ip, city=response.city, country=response.country, regoin=response.region, deviceType=device_type)
        except:
            pass
        # print(user_agent)
        return HttpResponseRedirect(env("OTHER_URL"))
