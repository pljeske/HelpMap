from django.shortcuts import render
from social.models import *


def show_messages(request):
    context = {"page_title": "My Messages"}
    # get last message first
    messages = Message.objects.filter(receiver=request.user).order_by('-date')
    context["mails"] = messages
    return render(request, "messages/my_messages.html", context)

