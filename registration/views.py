from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from registration.forms import *


def change_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = User.objects.get(id=request.user.id).profile

            try:
                profile.picture = profile_form.cleaned_data.get("picture")
                print(profile.picture)
            except Exception as e:
                print(e)
            try:
                profile.description = profile_form.cleaned_data.get("description")
            except Exception as e:
                print(e)
            try:
                profile.save() #SUCCESS MELDUNG
            except Exception as e:
                pass #FEHLERMELDUNG
    else:
        profile_form = ProfileForm()

    context = {
        "form": profile_form
    }
    return render(request, "registration/change-profile.html", context)


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