from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Point
from .nearest_point import find_nearest_point
from .serializers import PointSerializer, NearestPointSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class NearestPointViewSet(viewsets.ViewSet):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="lat", description="Latitude", required=True, type=float
            ),
            OpenApiParameter(
                name="lon", description="Longitude", required=True, type=float
            ),
        ],
        responses=NearestPointSerializer,
    )
    @action(detail=False, methods=["get"])
    def find(self, request: Request) -> Response:
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")
        nearest_point = find_nearest_point(lat, lon)
        if isinstance(nearest_point, Response):
            return nearest_point
        serializer = NearestPointSerializer(nearest_point)
        print(type(Response(serializer.data)))
        print(type(request))
        return Response(serializer.data)
