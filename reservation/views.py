from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Reservation
from django.urls import reverse_lazy

# Landing page view for testing and debugging
def ice_reservation_home(request):
    return render(request, 'reservation/mo_calendar.html')

class IceReservationCreateView(CreateView):
    """
    A view for creating a new `Reservation` instance.

    Utilizes Django's generic CreateView to provide a form for creating a new reservation
    related to ice booking. On successful form submission, redirects to a success URL.
        
    """
  
    model = Reservation
    fields = ['ice_customer', 'ice_time_slot', 'date', 'ice_status', 'is_cancelable']
    success_url = reverse_lazy('reservation_success')

