from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from HelpMap import settings
from registration.forms import *
from django.contrib import messages


@login_required(redirect_field_name='next', login_url="/account/login")
def change_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES)
        try:
            validate_image_file_extension(request.FILES.get("picture"))
        except Exception as e:
            messages.add_message(request, messages.ERROR, "Es sind nur Bilder erlaubt!")
        if profile_form.is_valid():
            profile = User.objects.get(id=request.user.id).profile
            try:
                profile.picture = profile_form.files.get("picture")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Der Upload ist leider fehlgeschlagen!")
            try:
                profile.save()
                messages.add_message(request, messages.SUCCESS, "Ihr Bild wurde erfolgreich hochgeladen!")
            except Exception as e:
                messages.add_message(request, messages.ERROR, "Aktuell können wir nicht auf Ihr Profuil zugreifen. Bitte versuchen Sie es später erneut!")
        return redirect("profile")
    else:
        profile_form = ProfileForm()
        context = {
            "page_title": "Neues Profilbild hochladen",
            "form": profile_form
        }
        return render(request, "account/change-profile.html", context)


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
    return render(request, "account/register.html", context)


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
                if request.POST.get("next"):
                    return HttpResponseRedirect(request.POST.get("next"))
                else:
                    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        context["form"] = form
        messages.add_message(request, messages.ERROR, "Ungültige Anmeldedaten!")
        return render(request, "account/login.html", context)
    else:
        form = LoginForm()
        context["form"] = form
        return render(request, "account/login.html", context)


def do_logout(request):
    logout(request)
    return redirect("index")
