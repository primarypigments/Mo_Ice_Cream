from django.contrib import admin
from .models import Reservation
from .models import ContactMessage


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("customer", "date", "time_slot", "location", "status")


admin.site.register(ContactMessage)