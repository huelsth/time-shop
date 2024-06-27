from django.contrib import admin
from .models import TimeModel, Booking, CustomerProfile

admin.site.register(TimeModel)
admin.site.register(Booking)
admin.site.register(CustomerProfile)
