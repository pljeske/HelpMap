from social.models import *
from django import forms


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput)
