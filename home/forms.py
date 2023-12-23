
from .models import *
from django import forms
from product.models import *
from django.utils.translation import gettext_lazy as _


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
