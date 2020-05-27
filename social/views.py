from django.http import JsonResponse
from django.shortcuts import render, redirect
from social.forms import *
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import permissions
from social.serializers import MessageSerializer
import datetime


def get_messages_rest(request, user_id):
    if request.method == 'GET' and request.user.is_authenticated:
        other_user = User.objects.get(id=user_id)
        messages_sender = Message.objects.filter(sender=request.user, receiver=other_user)
        messages_receiver = Message.objects.filter(sender=other_user, receiver=request.user)
        mails = (messages_sender | messages_receiver).order_by('date')
        serializer = MessageSerializer(mails, many=True)
        return JsonResponse(serializer.data, safe=False)


def show_profile(request):
    user = request.user
    return show_other_profile(request, user.id)


def show_other_profile(request, user_id):
    if request.user.is_authenticated:
        other_user = User.objects.get(id=user_id)
        own_profile = (request.user == other_user)
        context = {
            "user": request.user,
            "other_user": other_user,
            "own_profile": own_profile
        }
        if own_profile:
            own_points = HelpPoint.objects.all().filter(author=request.user)
            context["own_points"] = own_points
        return render(request, "account/profile.html", context)
    else:
        messages.add_message(request, messages.ERROR, "You must be logged in to do that!")
        return redirect("login")


def show_messages(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "You have to be logged in to do that!")
        return redirect("login")

    context = {"page_title": "Messages"}

    messages_receiver = Message.objects.filter(receiver=request.user)
    messages_sender = Message.objects.filter(sender=request.user)
    mails = messages_receiver | messages_sender

    # open the messages page from user with last message
    if mails.count() > 0:
        mails = mails.order_by('-date')
        if mails.first().receiver != request.user:
            user_id = mails.first().receiver.id
        else:
            user_id = mails.first().sender.id
        return message_handler(request, user_id)
    else:
        context["other_user"] = "everyone"
        context["user"] = request.user
        return render(request, "messages/messages_rest.html", context)


def message_handler(request, user_id):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, "You have to be logged in to do that!")
        return redirect("login")
    other_user = User.objects.get(id=user_id)
    messages_sender = Message.objects.filter(sender=request.user, receiver=other_user)
    messages_receiver = Message.objects.filter(sender=other_user, receiver=request.user)
    mails = (messages_sender | messages_receiver).order_by('date')

    unread_from = request.user.profile.unread_messages_from.all()

    try:
        request.user.profile.unread_messages_from.remove(other_user.id)
    except Exception as e:
        print(e)

    form = MessageForm()

    if request.method == "POST":
        text = request.POST["message"]
        receiver = User.objects.get(id=user_id)
        message = Message(sender=request.user, receiver=receiver, text=text)
        message.save()

        user_interaction1, created1 = UserInteraction.objects.get_or_create(user=request.user)
        user_interaction2, created2 = UserInteraction.objects.get_or_create(user=receiver)

        user_interaction1.others.add(receiver)
        user_interaction2.others.add(request.user)
        # user_interaction1.last_interaction = datetime.datetime.now()
        # user_interaction2.last_interaction = datetime.datetime.now()
        user_interaction1.save()
        user_interaction2.save()

        receiver.profile.unread_messages_from.add(request.user)
    try:
        users_interactions = UserInteraction.objects.get(user=request.user).others
    except UserInteraction.DoesNotExist:
        users_interactions = []

    context = {"page_title": "Messages " + other_user.username,
               "mails": mails,
               "form": form,
               "other_user": other_user,
               "user_interactions": users_interactions,
               "user": request.user,
               "unread_from": unread_from}

    return render(request, "messages/messages_rest.html", context)
