from django.test import TestCase

from api.models import Point


class PointModelTestCase(TestCase):
    def setUp(self):
        Point.objects.create(name="Test-point-1", description="This is test point 1", geom="POINT (5 23)")
        Point.objects.create(name="Test-point-2", description="This is test point 2", geom="POINT (2 9)")

    def test_create_point(self):
        point1 = Point.objects.get(name="Test-point-1")
        point2 = Point.objects.get(name="Test-point-2")
        self.assertEqual(point1.description, "This is test point 1")
        self.assertEqual(point2.description, "This is test point 2")
