from django import forms
from map.models import *


class NewHelpPointForm(forms.Form):
    street = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Alexanderplatz 1'}))
    zip_and_city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '10178 Berlin'}))
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Description', 'rows': '8'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())
