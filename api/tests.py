from django.test import TestCase
from rest_framework.test import APITestCase
from api.models import Point
from django.urls import reverse

from api.nearest_point import find_nearest_point
from api.serializers import PointSerializer


class PointModelTestCase(TestCase):
    def setUp(self):
        Point.objects.create(name="Test-point-1", description="This is test point 1", geom="POINT (5 23)")
        Point.objects.create(name="Test-point-2", description="This is test point 2", geom="POINT (2 9)")

    def test_create_point(self):
        point1 = Point.objects.get(name="Test-point-1")
        point2 = Point.objects.get(name="Test-point-2")
        self.assertEqual(point1.description, "This is test point 1")
        self.assertEqual(point2.description, "This is test point 2")


class PointViewSetTestCase(APITestCase):
    def setUp(self):
        Point.objects.create(name="Test-point-1", description="This is test point 1", geom="POINT (5 23)")
        Point.objects.create(name="Test-point-2", description="This is test point 2", geom="POINT (2 9)")

    def test_get_all_point(self):
        response = self.client.get(reverse("api:point-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_point(self):
        data = {
            "name": "Test-point-3",
            "description": "This is test point 3",
            "geom": "POINT (3 11)",
        }
        response = self.client.post(reverse("api:point-list"), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Point.objects.count(), 3)


class PointSerializerTestCase(TestCase):
    def setUp(self):
        self.point = Point.objects.create(name="Test-point-1", description="This is test point 1", geom="POINT (5 23)")
        self.serializer = PointSerializer(instance=self.point)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ["id", "name", "description", "geom"])


class NearestPointTestCase(TestCase):
    def setUp(self):
        Point.objects.create(name="Test-point-1", description="This is test point 1", geom="POINT (5 23)")
        Point.objects.create(name="Test-point-2", description="This is test point 2", geom="POINT (2 9)")

    def test_find_nearest_point(self):
        point = find_nearest_point(4, 6)
        self.assertEqual(point.name, "Test-point-2")
