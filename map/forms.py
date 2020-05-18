from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from registration.models import *
from map.models import *
from leaflet.forms.widgets import LeafletWidget


class AddHelpPointForm(forms.Form):
    street = forms.CharField()
    street_nr = forms.CharField()
    zip = forms.CharField()
    city = forms.CharField()
    title = forms.CharField()
    description = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
