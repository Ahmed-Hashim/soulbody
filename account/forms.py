from django import forms
from django.forms import PasswordInput
from .models import ClientUser


class ClientUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    password1 = forms.CharField(label="Confirm Password", widget=PasswordInput)

    class Meta:
        model = ClientUser
        fields = ["email", "first_name", "last_name", "password"]

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords do not match.")

        return password1
