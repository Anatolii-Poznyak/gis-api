from rest_framework import serializers
from rest_framework_gis.serializers import GeometryField

from api.models import Point


class PointSerializer(serializers.ModelSerializer):
    geom = GeometryField()

    class Meta:
        model = Point
        fields = "id", "name", "description", "geom"


class NearestPointSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Point
        fields = "id", "name", "description", "geom", "distance"

    @staticmethod
    def get_distance(obj):
        return obj.distance.m

