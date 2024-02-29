import json
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Reservation
from django.urls import reverse_lazy
from django.http import JsonResponse
import datetime
import logging

logger = logging.getLogger(__name__)

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
    # Accepting a date parameter from the request
    date_str = request.GET.get('date', None)
    if date_str is None:
        return JsonResponse({'status': 'error', 'message': 'Date parameter is required.'}, status=400)

    try:
        # I need to verify if Fullcalendar sends in ISO 8601 format;
        reservation_date = datetime.datetime.fromisoformat(date_str).date()
    except ValueError:
        return JsonResponse({'status': 'error', 'message': 'Invalid date format.'}, status=400)

    # Fetching reservations for the specific date
    reservations = Reservation.objects.filter(date=reservation_date)

    # Formatting the reservations data for use
    events = [{
        "title": reservation.ice_customer,
        "start": reservation.ice_time_slot.isoformat(),
        "end": (reservation.ice_time_slot + datetime.timedelta(hours=4)).isoformat(),
    } for reservation in reservations]

    return JsonResponse(events, safe=False)


@csrf_exempt
def submit_ice_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data.pop('ice_status', None)  # Ensure 'ice_status' is not in the request body

            try:
                default_status = IceReservationStatus.objects.get(ice_status='pending')
            except IceReservationStatus.DoesNotExist:
                logger.error("Default IceReservationStatus 'pending' does not exist.")
                return JsonResponse({'status': 'error', 'message': 'Internal server error: Default reservation status not found.'}, status=500)

            form = ReservationForm(data)
            if form.is_valid():
                try:
                    with transaction.atomic():
                        reservation_instance = form.save(commit=False)
                        reservation_instance.ice_status = default_status
                        reservation_instance.save()
                        return JsonResponse({'status': 'success', 'message': 'Reservation submitted successfully.'}, status=200)
                except IntegrityError as e:
                    logger.error(f"Database integrity error when saving reservation: {e}")
                    return JsonResponse({'status': 'error', 'message': 'Internal server error: Database operation failed.'}, status=500)
            else:
                logger.error(f"Form validation error: {form.errors.as_json()}")
                return JsonResponse({'status': 'error', 'message': form.errors.as_json()}, status=400)
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error in request body: {e}")
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({'status': 'error', 'message': 'Internal server error.'}, status=500)
    else:
        logger.warn("Attempted non-POST request to submit_ice_reservation.")
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)