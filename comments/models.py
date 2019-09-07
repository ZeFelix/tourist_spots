from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):

        return  self.user.get_short_name()

