from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views import PointViewSet

router = DefaultRouter()
router.register(r"points", viewset=PointViewSet, basename="point")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "api"
