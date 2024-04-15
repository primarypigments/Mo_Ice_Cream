from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    """
    Custom DateInput widget for form fields,
    rendering them with 'date' type inputs.
    """
    input_type = "date"


class ReservationForm(forms.ModelForm):
    """
    Form for creating or updating a Reservation,
    utilizing custom widgets for date fields.
    """

    class Meta:
        model = Reservation
        widgets = {
            "date": DateInput(),
        }
        fields = ("phone_number", "date", "time_slot", "location")


class CancelReservationForm(forms.Form):
    """
    Form to capture the reason for a reservation cancellation,
    with an optional text area.
    """
    reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder':
     'Reason for cancellation (optional)'}), required=False)
