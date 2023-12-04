from .models import*
from django import forms

class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        