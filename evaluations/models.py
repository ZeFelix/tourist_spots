from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Evaluations(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    note = models.DecimalField(decimal_places=2,max_digits=5)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user.get_short_name()
