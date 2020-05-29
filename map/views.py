from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from opencage.geocoder import OpenCageGeocode
from map.forms import *
from map.models import *
from social.views import show_profile
from django.contrib.gis.geoip2 import GeoIP2
from config.project_config import OPENCAGE_API_KEY


def index(request):
    location = get_client_location(request)
    help_points = HelpPoint.objects.all()
    context = {
        "page_title": "Map",
        "help_points": help_points,
        "user_location": location
    }
    return render(request, "map/map.html", context)


@login_required(redirect_field_name='next', login_url="/account/login")
def new_help_point(request):
    context = {"page_title": "Offer Help"}
    if request.method == "POST":
        form = NewHelpPointForm(request.POST)
        if form.is_valid():
            try:
                street_and_nr = form.cleaned_data.get("street")
                zip_and_city = form.cleaned_data.get("zip_and_city")
                title = form.cleaned_data.get("title")
                description = form.cleaned_data.get("description")
                category = Category.objects.all().filter(title=form.cleaned_data.get("category"))[0]
                point = get_lat_long(street_and_nr, zip_and_city)
                map_point = {
                    'type': 'Point',
                    'coordinates': point
                }

                new_point = HelpPoint(author=request.user, title=title, description=description, geom=map_point,
                                      category=category)
                new_point.save()
                context["form"] = form
                context["saved_point"] = new_point
                messages.add_message(request, messages.SUCCESS, "Your point has been added!")
                return render(request, "map/add_help_point.html", context)

            except Exception as e:
                messages.add_message(request, messages.ERROR, e)
                context["form"] = form
        else:
            messages.add_message(request, messages.ERROR, "Form is invalid!")
            context["form"] = form
    else:
        form = NewHelpPointForm()
        context["form"] = form
        return render(request, "map/add_help_point.html", context)
    return render(request, "map/add_help_point.html", context)


@login_required(redirect_field_name='next', login_url="/account/login")
def delete_help_point(request, point_id):
    try:
        help_point = HelpPoint.objects.get(id=point_id)
        if help_point.author == request.user:
            help_point.delete()
            messages.add_message(request, messages.SUCCESS, "Your entry was deleted!")
        else:
            messages.add_message(request, messages.ERROR, "You can only delete your own entries!")
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Something went wrong while deleting your entry!")
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
    print(x_forwarded_for)
    print(remote_address)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        location = GeoIP2().lon_lat(ip)
        print(location)
    elif remote_address and remote_address != "127.0.0.1":
        location = GeoIP2().lon_lat(remote_address)
    else:
        location = (13.404954, 52.520008)
    return (location[1], location[0])
