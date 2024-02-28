from . import views
from django.urls import path
from .views import IceReservationCreateView, ice_reservation_home, available_ice_slots, submit_ice_reservation


urlpatterns = [
    path('', ice_reservation_home, name='ice_reservation_home'),
    path('availability/', available_ice_slots, name='availability'),
    path('submit_ice_reservation/', submit_ice_reservation, name='submit_ice_reservation'),
]
