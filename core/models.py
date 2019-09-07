from django.db import models

from attractions.models import Attractions
from comments.models import Comments
from evaluations.models import Evaluations


class TouristSpots(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comments = models.ForeignKey(Comments, on_delete=models.SET_NULL, blank=True, null=True)
    evaluations = models.ManyToManyField(Evaluations)

    def __str__(self):

        return self.name