from django.core.exceptions import ValidationError
from django.utils import timezone
import re


def validate_future_date(value):
    today_date = timezone.localdate()  # Get today's date
    if value < today_date:
        raise ValidationError(
            "The date selected has already passed. Please try again.")


def validate_phone_number(value):
