from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from registration.forms import *
from django.contrib import messages


def change_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = User.objects.get(id=request.user.id).profile
            try:
                profile.picture = profile_form.files.get("picture")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Something went wrong while uploading!")
            try:
                profile.save()
                messages.add_message(request, messages.SUCCESS, "Your picture was uploaded!")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Something went wrong while uploading!")
        return redirect("profile")
    else:
        profile_form = ProfileForm()
        context = {
            "page_title": "Upload Profile Picture",
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
        context["form"] = form
        messages.add_message(request, messages.ERROR, "Invalid login data!")
        return render(request, "registration/login.html", context)
    else:
        form = LoginForm()
        context["form"] = form
        return render(request, "registration/login.html", context)


def do_logout(request):
    logout(request)
    return redirect("index")
