from django.shortcuts import render, redirect
from django.contrib import messages
from map.forms import *
from geopy.geocoders import Nominatim
from geopy.location import Location
from map.models import HelpPoint
from map.models import *


def index_old(request):
    context = {"page_title": "Map"}
    mapbox_access_token = 'pk.my_mapbox_access_token'
    context["mapbox_access_token"] = 'pk.eyJ1IjoicGxqY2dtIiwiYSI6ImNrOWxnNTltbjA3NmYzbHEwamQxc2Z4YmsifQ.sHPPkFf2k1KDreY5bRIX2A'
    return render(request, "map/map_old.html", context)


def index(request):
    context = {"page_title": "Map"}
    help_points = HelpPoint.objects.all()
    context["help_points"] = help_points
    return render(request, "map/map.html", context)


def add_help_point(request):
    if request.user.is_authenticated:
        context = {"page_title": "Add Help Point"}
        if request.method == "POST":
            form = AddHelpPointForm(request.POST)
            if form.is_valid():
                try:
                    street = form.cleaned_data.get("street")
                    street_nr = form.cleaned_data.get("street_nr")
                    zip_code = form.cleaned_data.get("zip")
                    city = form.cleaned_data.get("city")
                    description = form.cleaned_data.get("description")
                    point = get_lat_long(street, street_nr, zip_code)

                    category = Category.objects.all().filter(title=form.cleaned_data.get("category"))
                    category = category[0]
                    author = request.user

                    map_point = {
                        'type': 'Point',
                        'coordinates': point
                    }

                    try:
                        new_point = HelpPoint(author=author, title=description, geom=map_point, category=category)
                        new_point.save()
                        context["form"] = form
                        context["saved_point"] = new_point
                        messages.add_message(request, messages.SUCCESS, "Your point has been added!")
                        return render(request, "map/add_help_point.html", context)
                    except Exception as e:
                        messages.add_message(request, messages.ERROR, e)
                        context["form"] = form
                except Exception as e:
                    messages.add_message(request, messages.ERROR, e)
                    context["form"] = form
            else:
                messages.add_message(request, messages.ERROR, "Form is invalid!")
                context["form"] = form
        else:
            form = AddHelpPointForm()
            context["form"] = form
            return render(request, "map/add_help_point.html", context)
        return render(request, "map/add_help_point.html", context)
    else:
        messages.add_message(request, messages.ERROR, "You have to be logged in to do that!")
        return redirect("login")


def who(request):
    context = {"page_title": "Who"}
    return render(request, "who.html", context)


def create_entry(request):
    context = {"page_title": "Help"}
    return render(request, "map/help.html", context)


def get_lat_long(street, nr, zip):
    nominatim = Nominatim(user_agent="help_map")

    query = {
        "street": street,
        "country": "DE",
        "postalcode": zip,
        "houseNumber": nr
    }

    result = nominatim.geocode(query=query, exactly_one=True)
    print(result)

    return [result.longitude, result.latitude]
