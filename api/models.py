from django.contrib.gis.db import models


class Point(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    geom = models.PointField(unique=True)
