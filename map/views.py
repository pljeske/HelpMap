from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.contrib import messages
from map.forms import *
from map.models import *
from social.views import show_profile


def index(request):
    context = {
        "page_title": "Startseite"
    }
    return render(request, "index.html", context)


def map(request):
    help_points = HelpPoint.objects.all()
    context = {
        "page_title": "Karte",
        "help_points": help_points,
    }
    return render(request, "map/map.html", context)


@login_required(redirect_field_name='next', login_url="/account/login")
def new_help_point(request):
    html_file = "map/add_help_point.html"
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
                    return render(request, html_file, context)
                point_list = point.split(",")
                map_point = {
                    'type': 'Point',
                    'coordinates': [point_list[1], point_list[0]]
                }

                new_point = HelpPoint(author=request.user, title=title, description=description, geom=map_point,
                                      category=category)
                new_point.save()
                context["form"] = form
                messages.add_message(request, messages.SUCCESS, "Der Punkt wurde der Karte hinzugefügt")
                return render(request, html_file, context)

            except Exception as e:
                messages.add_message(request, messages.ERROR, e)
                context["form"] = form
        else:
            messages.add_message(request, messages.ERROR, "Bitte füllen Sie alle Felder aus und wählen Sie einen Standort!")
            context["form"] = form
    else:
        form = NewHelpPointForm()
        context["form"] = form
        return render(request, html_file, context)
    return render(request, html_file, context)


def show_help_point(request, offer_id):
    html_file = "map/help_point_single.html"
    try:
        help_point = HelpPoint.objects.get(id=offer_id)
    except HelpPoint.DoesNotExist:
        raise Http404("Der Helppoint ist aktuell nicht verfügbar.")

    context = {
        "page_title": help_point.title,
        "help_point": help_point
    }
    return render(request, html_file, context)


@login_required(redirect_field_name='next', login_url="/account/login")
def delete_help_point(request, point_id):
    try:
        help_point = HelpPoint.objects.get(id=point_id)
        if help_point.author == request.user:
            help_point.delete()
            messages.add_message(request, messages.SUCCESS, "Das Angebot wurde gelöscht")
        else:
            messages.add_message(request, messages.ERROR, "Sie können nur die mit Ihrem Nutzerkonto verknüpften Angebote löschen.")
    except Exception:
        messages.add_message(request, messages.ERROR, "Leider ist beim Löschen ein Fehler aufgetreten.")
    return show_profile(request)


def get_info(request):
    context = {"page_title": "Info"}
    return render(request, "info.html", context)
