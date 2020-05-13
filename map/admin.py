from django.contrib import admin

# Register your models here.
from leaflet.admin import LeafletGeoAdmin
from map.models import *

admin.site.register(HelpPoint, LeafletGeoAdmin)
admin.site.register(Category)
