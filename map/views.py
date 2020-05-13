from django.shortcuts import render


def index(request):
    context = {"page_title": "Map"}
    mapbox_access_token = 'pk.my_mapbox_access_token'
    context["mapbox_access_token"] = 'pk.eyJ1IjoicGxqY2dtIiwiYSI6ImNrOWxnNTltbjA3NmYzbHEwamQxc2Z4YmsifQ.sHPPkFf2k1KDreY5bRIX2A'
    return render(request, "map/map.html", context)


def who(request):
    context = {"page_title": "Who"}
    return render(request, "who.html", context)


def create_entry(request):
    context = {"page_title": "Help"}
    return render(request, "map/help.html", context)