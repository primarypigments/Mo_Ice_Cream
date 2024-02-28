from django.conf import settings
from django.db import models

class IceReservationStatus(models.Model):
    """
    Represents the status of an ice reservations, categorizing the reservation's
    current state (pending, confirmed, or canceled).

    """
    ice_status = models.CharField(max_length=100)
    description_ice = models.TextField()

    def __str__(self):
        return self.status

class Reservation(models.Model): 
    """
    Stores a single reservation related to model auth.User and model IceReservationStatus.

    This model keeps track of all necessary details for an ice reservation including the ice customer
    details, time slot, status, and if the reservation is cancelable.


    """
    ice_customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ice_customer_name = models.CharField(max_length=100, default='No Name Provided') #Need to add valivation on a later note
    ice_customer_email = models.EmailField(default='non_helper@example.com')
    ice_time_slot = models.CharField(max_length=50)
    date = models.DateField()
    ice_status = models.ForeignKey(IceReservationStatus, on_delete=models.CASCADE)
    is_cancelable = models.BooleanField(default=True)

    def __str__(self):
       return f"Reservation for {self.ice_customer_name} on {self.date} at {self.ice_time_slot}"
