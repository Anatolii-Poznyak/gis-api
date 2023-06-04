from django.contrib.gis.db import models


class Point(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    geom = models.PointField()
