from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = "date"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        widgets = {
            "date": DateInput(),
        }
        fields = ("phone_number", "date", "time_slot", "location")


class CancelReservationForm(forms.Form):
    reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder':
     'Reason for cancellation (optional)'}), required=False)
