from django.apps import AppConfig


class IndexConfig(AppConfig):
    """
    Configuration class for the 'index' app.
    It specifies the default auto field type
    to be used for model IDs across the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
