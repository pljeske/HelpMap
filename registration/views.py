from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from registration.forms import *


def do_register(request):
    context = {"page_title": "Registration"}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect("index")
        else:
            context["form"] = form
    else:
        form = RegistrationForm()
        context["form"] = form
    return render(request, "registration/register.html", context)


def do_login(request):
    context = {"page_title": "Login"}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            account = authenticate(username=username, password=raw_password)
            if account is not None:
                login(request, account)
                return redirect("index")
            else:
                context["form"] = form
        else:
            context["form"] = form
    else:
        form = LoginForm()
        context["form"] = form
        return render(request, "registration/login.html", context)


def do_logout(request):
    logout(request)
    return redirect("index")