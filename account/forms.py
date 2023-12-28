from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "jobtitle",
            "fullname",
            "bio",
            "phone_number",
            "gender",
            "country",
            "address",
            "facebook_url",
            "instagram_url",
            "twitter_url",
            "linkedin_url",
            "skype_url",
        )

        widgets = {
            "jobtitle": forms.TextInput(attrs={"class": "form-control"}),
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.Textarea(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "facebook_url": forms.TextInput(attrs={"class": "form-control"}),
            "instagram_url": forms.TextInput(attrs={"class": "form-control"}),
            "twitter_url": forms.TextInput(attrs={"class": "form-control"}),
            "linkedin_url": forms.TextInput(attrs={"class": "form-control"}),
            "skype_url": forms.TextInput(attrs={"class": "form-control"}),
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )


class ClientUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    password1 = forms.CharField(label="Confirm Password", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords do not match.")

        return password1


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )


class CartItemForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={"class": "cart-plus-minus-box"}),
    )
