from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from opencage.geocoder import OpenCageGeocode
from map.forms import *
from map.models import *
from social.views import show_profile
from django.contrib.gis.geoip2 import GeoIP2
from config.project_config import OPENCAGE_API_KEY


def index(request):
    context = {
        "page_title": "Startseite"
    }
    return render(request, "index.html", context)


def map(request):
    location = get_client_location(request)
    help_points = HelpPoint.objects.all()
    context = {
        "page_title": "Karte",
        "help_points": help_points,
        "user_location": location
    }
    return render(request, "map/map.html", context)


@login_required(redirect_field_name='next', login_url="/account/login")
def new_help_point(request):
    context = {"page_title": "Hilfe anbieten"}
    if request.method == "POST":
        form = NewHelpPointForm(request.POST)
        if form.is_valid():
            try:
                title = form.cleaned_data.get("title")
                description = form.cleaned_data.get("description")
                category = Category.objects.all().filter(title=form.cleaned_data.get("category"))[0]
                point = form.cleaned_data.get("location")
                if point is None:
                    messages.add_message(request, messages.ERROR, "Standort fehlerhaft!")
                    context["form"] = form
                    return render(request, "map/add_help_point.html", context)
                point_list = point.split(",")
                map_point = {
                    'type': 'Point',
                    'coordinates': [point_list[1], point_list[0]]
                }

                new_point = HelpPoint(author=request.user, title=title, description=description, geom=map_point,
                                      category=category)
                new_point.save()
                context["form"] = form
                context["saved_point"] = new_point
                messages.add_message(request, messages.SUCCESS, "Der Punkt wurde der Karte hinzugefügt")
                return HttpResponseRedirect("/map/add_help_point_success.html", context)

            except Exception as e:
                messages.add_message(request, messages.ERROR, e)
                context["form"] = form
        else:
            messages.add_message(request, messages.ERROR, "Bitte füllen Sie alle Felder aus und wählen Sie einen Standort!")
            context["form"] = form
    else:
        form = NewHelpPointForm()
        context["form"] = form
        return render(request, "map/add_help_point.html", context)
    return render(request, "map/add_help_point.html", context)


def show_help_point(request, offer_id):
    try:
        help_point = HelpPoint.objects.get(id=offer_id)
    except HelpPoint.DoesNotExist:
        raise Http404("Der Helppoint ist aktuell nicht verfügbar.")

    context = {
        "page_title": help_point.title,
        "help_point": help_point
    }

    return render(request, "map/offer_help/success", context)


@login_required(redirect_field_name='next', login_url="/account/login")
def delete_help_point(request, point_id):
    context = {
        "page_title": "Helppoint löschen"
    }
    try:
        help_point = HelpPoint.objects.get(id=point_id)
        if help_point.author == request.user:
            help_point.delete()
            messages.add_message(request, messages.SUCCESS, "Das Angebot wurde gelöscht")
        else:
            messages.add_message(request, messages.ERROR, "Sie können nur die mit Ihrem Nutzerkonto verknüpften Angebote löschen.")
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Leider ist beim Löschen ein Fehler aufgetreten.")
    return show_profile(request)


def get_info(request):
    context = {"page_title": "Info"}
    return render(request, "info.html", context)


def get_lat_long(street_and_nr, zip_and_city):
    geocoder = OpenCageGeocode(OPENCAGE_API_KEY)
    query = ", ".join([street_and_nr, zip_and_city])
    results = geocoder.geocode(query)[0]['geometry']
    return [results['lng'], results['lat']]


def get_client_location(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    remote_address = request.META.get('REMOTE_ADDR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        location = GeoIP2().lon_lat(ip)
    elif remote_address and remote_address != "127.0.0.1":
        location = GeoIP2().lon_lat(remote_address)
    else:
        location = (13.404954, 52.520008)
    return (location[1], location[0])


def new_help_point_success(request):
    context = {"page_title": "Punkt erfolgreich hinzugefügt."}
    return render(request, "map/add_help_point_success.html", context)