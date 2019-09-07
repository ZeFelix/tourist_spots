from django.db import models

from attractions.models import Attractions


class TouristSpots(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)

    def __str__(self):

        return self.name