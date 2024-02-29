from . import views
from django.urls import path


urlpatterns = [
    path('', views.reservation_page, name='ice_reservation_page'),
]
