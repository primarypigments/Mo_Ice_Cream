from django.db import models
from django.contrib.auth.models import User
from .validators import validate_phone_number, validate_future_date


class Reservation(models.Model):
    """
    Custom model to have users book a reservation at Mo Ice Cream
    """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservations')
    phone_number = models.CharField(
    max_length=17, validators=[
        validate_phone_number], null=False, blank=False)
    date = models.DateField(
        null=False, blank=False, validators=[validate_future_date])
    time_slot = models.CharField(max_length=10, choices=[
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    ], null=False, blank=False)
    location = models.CharField(max_length=25, choices=[
        ('Kakenstorf', 'Kakenstorf'),
        ('Regesbostel', 'Regesbostel'),
        ('Brackel', 'Brackel'),
        ('Wistedt', 'Wistedt'),
        ('Eyendorf', 'Eyendorf'),
    ], null=False, blank=False)
    status = models.CharField(max_length=10, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Canceled', 'Canceled'),
    ], default="Pending")
    book_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time_slot', 'location')
#https://docs.djangoproject.com/en/4.2/ref/models/options/#unique-together
    def __str__(self):
        return self.date.strftime("%B %d, %Y")


class ContactMessage(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField(max_length=350)
    submitted_at = models.DateTimeField(auto_now_add=True)
#https://docs.djangoproject.com/en/4.2/ref/models/database-functions/
