from .models import *
from django import forms
from product.models import *


class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class Request_Clinic_form(forms.ModelForm):
    class Meta:
        model = RequestClinicSystemPackage
        fields = "__all__"
