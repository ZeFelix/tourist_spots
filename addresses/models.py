from django.db import models

# Create your models here.

class Addresses(models.Model):
    address_one = models.CharField(max_length=150)
    address_two = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    lat = models.IntegerField(blank=True, null=True)
    long = models.IntegerField(blank=True, null=True)

    def __str__(self):

        return self.address_one