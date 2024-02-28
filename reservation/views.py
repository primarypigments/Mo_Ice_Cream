import json
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Reservation
from django.urls import reverse_lazy
from django.http import JsonResponse
import datetime
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt


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


def available_ice_slots(request):
    # Assuming you want to fetch reservations for a specific range
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=30)  # Adjust the range as needed

    # Fetching reservations within the specified date range
    reservations = Reservation.objects.filter(date__range=(start_date, end_date))

    # Formatting the reservations data for FullCalendar
    events = [
        {
            "title": "Unavailable",  # Or any title you want to show on the calendar
            "start": reservation.time_slot.isoformat(),
            "end": (reservation.time_slot + datetime.timedelta(hours=1)).isoformat(),  # Adjust according to your needs
        }
        for reservation in reservations
    ]

    return JsonResponse(events, safe=False)


@csrf_exempt
def submit_ice_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # i will need to  add validate data later
            reservation = Reservation(
                ice_customer_name=data['name'],
                ice_customer_email=data['email'],
                date=data['date'],
                ice_time_slot=data['timeSlot'],
                is_cancelable=True,
                
            )
            reservation.full_clean()  # Django's built-in model validation link ----  https://docs.djangoproject.com/en/5.0/ref/models/instances/
            reservation.save()
            return JsonResponse({'ice_status': 'success', 'message': 'Reservation submitted successfully.'}, status=200)
        except ValidationError as e:
            return JsonResponse({'status': 'error', 'message': e.messages}, status=400)
        except Exception as e:
            return JsonResponse({'ice_status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'ice_status': 'error', 'message': 'Invalid request'}, status=400)
