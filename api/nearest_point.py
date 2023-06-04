from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import status
from rest_framework.response import Response
from .models import Point


def find_nearest_point(lat, lon):
    try:
        user_location = Point(float(lon), float(lat), srid=4326)
    except ValueError:
        return Response({"detail": "Invalid coordinates"}, status=status.HTTP_400_BAD_REQUEST)
    nearest_point = Point.objects.annotate(
        distance=Distance("geom", user_location)
    ).order_by("distance").first()
    return nearest_point

