from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Pflichtfeld. Bitte geben Sie eine gültige Mailadresse an!")
    first_name = forms.CharField(max_length=100, required=True, )
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Passwort")


class ProfileForm(forms.Form):
    picture = forms.ImageField(required=True, label="Neues Profilbild hochladen")
    #description = forms.CharField(max_length=150, required=False, widget=forms.Textarea)