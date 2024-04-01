from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .forms import ReservationForm 
from .models import Reservation
import logging
from .forms import CancelReservationForm
from .models import ContactMessage


logger = logging.getLogger(__name__)


@login_required
def reservation_page(request):
    """Handles the reservation page view. This view is responsible for creating new reservations.
    
    The view uses the ReservationForm to collect reservation details. If the form is submitted (POST request) and
    is valid, it attempts to save a new reservation instance. If successful, it redirects the user to their profile page.
    If an IntegrityError (occurs the reservation slot is already booked), it displays an error message.
    
     """
    form = ReservationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.instance.customer = request.user
                form.save()
                messages.success(request, "Thanks for your reservation!")
                return redirect(reverse("profile"))
            except IntegrityError:
                messages.error(request, "The selected reservation slot is unavailable. Please choose a different date, time, or location.")
        else:
            messages.error(request, "The selected reservation slot is unavailable. Please choose a different date, time, or location.")

    template = "reservation/mo_calendar.html"
    context = {
        "form": form,
    }
    return render(request, template, context)



@login_required
def edit_reservation(request, id):
    """ Reservation page view for editing a reservation """
    reservation = get_object_or_404(Reservation, id=id)
    if reservation.customer != request.user:
        # invalid user/customer
        messages.error(request, "Access denied, this is not your reservation")
        return redirect(reverse("index"))

    # logged-in user owns this reservation and can proceed
    form = ReservationForm(request.POST or None, instance=reservation)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Reservation updated!")
            return redirect(reverse("profile"))
        messages.error(request, "Error: Please try again.")

    template = "reservation/edit_reservation.html"
    context = {
        "reservation": reservation,
        "form": form,
    }
    return render(request, template, context)


@login_required
def delete_reservation(request, id):
    """Reservation page view for deleting a reservation with confirmation."""
    reservation = get_object_or_404(Reservation, id=id)

    if reservation.customer != request.user:
        messages.error(request, "Access denied, this is not your reservation")
        return redirect(reverse("index"))

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Reservation deleted!")
        return redirect(reverse("profile"))

    return render(request, 'reservation/delete_reservation_confirm.html', {'reservation': reservation})


@login_required
def cancel_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)

    if reservation.customer != request.user:
        messages.error(request, "Access denied, this is not your reservation")
        return redirect(reverse("index"))

    if request.method == 'POST':
        form = CancelReservationForm(request.POST)
        if form.is_valid():
            reservation.status = 'Canceled'
            reservation.save()
            messages.success(request, "Your reservation has been canceled.")
            # Redirect to a confirmation page or profile
            return redirect(reverse("profile"))
    else:
        form = CancelReservationForm()

    context = {
        'form': form,
        'reservation': reservation
    }
    return render(request, 'reservation/cancel_reservation_confirm.html', context)


@login_required
def profile(request):
    reservations = Reservation.objects.filter(customer=request.user)
    template = "reservation/profile.html"
    context = {
        "reservations": reservations,
    }
    return render(request, template, context)

def contact(request):
