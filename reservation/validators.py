from django.core.exceptions import ValidationError
from django.utils import timezone
import re


def validate_future_date(value):
    """
    Validates that a given date is not in the past.
    """
    today_date = timezone.localdate()  # Get today's date
    if value < today_date:
        raise ValidationError(
            "The date selected has already passed. Please try again.")


def validate_phone_number(value):
    """
    Validates that a given date is not in the past.
    """
    phone_number_validate = r'^\+?(49)?0?\d{9,17}$'
    if not re.match(phone_number_validate, value):
        raise ValidationError(
            "Phone number must be entered in the format "
            "'+111111111'. Maximum 17 digits.")
