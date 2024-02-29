from django.shortcuts import render
from .forms import ReservationForm 
from .models import Reservation
import logging


logger = logging.getLogger(__name__)


# # Reservation page view for testing and debugging
# def reservation_page(request):
#     return render(request, 'reservation/mo_calendar.html')
