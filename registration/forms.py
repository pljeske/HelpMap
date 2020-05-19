from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.models import *


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text="Required. Please submit a valid Email address!")
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    picture = forms.ImageField(required=True, label="Upload new profile picture")
    #description = forms.CharField(max_length=150, required=False, widget=forms.Textarea)