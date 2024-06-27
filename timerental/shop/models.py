from django.db import models
from django.contrib.auth.models import User

class TimeModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='time_models/')
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    time_model = models.ForeignKey(TimeModel, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('End time must be after start time')

    def __str__(self):
        return f'{self.time_model.name} booking by {self.user.username}'

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username
