from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.models import *
from map.models import *
from leaflet.forms.widgets import LeafletWidget


class AddHelpPointForm(forms.Form):
    street = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Street'}))
    street_nr = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Street Nr.'}))
    zip = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'City'}))
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Description', 'rows': '8'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
