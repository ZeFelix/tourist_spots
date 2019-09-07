from django.db import models

# Create your models here.

class Attractions(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    opening_hours = models.TimeField()
    minimum_age = models.IntegerField()

    def __str__(self):

        return self.name