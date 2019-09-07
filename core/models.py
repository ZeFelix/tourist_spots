from django.db import models

from addresses.models import Addresses
from attractions.models import Attractions
from comments.models import Comments
from evaluations.models import Evaluations


class TouristSpots(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comments = models.ManyToManyField(Comments)
    evaluations = models.ManyToManyField(Evaluations)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):

        return self.name