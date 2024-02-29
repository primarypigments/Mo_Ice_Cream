from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['ice_customer_name', 'ice_customer_email', 'date', 'ice_time_slot', 'is_cancelable']
        
        