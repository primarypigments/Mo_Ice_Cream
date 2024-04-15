from django.apps import AppConfig


class IceReservationConfig(AppConfig):
    """
    AppConfig for the Ice Reservation module,
    defining default settings for model
    identifiers and the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'
