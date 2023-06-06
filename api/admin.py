from django.contrib import admin as admin_base
from django.contrib.gis import admin
from api.models import Point


@admin_base.register(Point)
class PlaceAdmin(admin.OSMGeoAdmin):
    list_display = ("id", "name", "description", "geom")
    search_fields = ("name",)
