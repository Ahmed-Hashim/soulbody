from product.admin import RequestHospitalSystemPackageAdmin
from .models import *
from django import forms
from product.models import *
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        label="Email*",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )


class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class Request_Clinic_form(forms.ModelForm):
    clinic_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        ),
    )
    departement_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )
    users_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )
    doctors_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )

    class Meta:
        model = RequestClinicSystemPackage
        fields = "__all__"


class Request_Hosbital_form(forms.ModelForm):
    hospital_beds_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )
    departement_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )
    users_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )
    doctors_count = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "cart-plus-minus-box",
                "name": "qtybutton",
                "value": "0",
            }
        )
    )

    class Meta:
        model = RequestHospitalSystemPackage
        fields = "__all__"
