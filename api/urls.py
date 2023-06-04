from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PointViewSet, NearestPointViewSet

router = DefaultRouter()
router.register("points", viewset=PointViewSet, basename="point")
router.register("nearest_point", viewset=NearestPointViewSet, basename="nearest_point")

urlpatterns = [path("", include(router.urls))]

app_name = "api"
