from django import forms
from map.models import *


class NewHelpPointForm(forms.Form):
    title = forms.CharField(label="Titel", widget=forms.TextInput(attrs={'placeholder': 'Titel Ihres Angebotes*'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Beschreibung*', 'rows': '8'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Kategorie*")
    location = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Standort', 'hidden': 'true'}))
