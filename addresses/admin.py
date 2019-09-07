from django.contrib import admin

# Register your models here.
from addresses.models import Addresses

admin.site.register(Addresses)