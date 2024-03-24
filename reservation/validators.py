from django.core.exceptions import ValidationError
from django.utils import timezone
import re


def validate_future_date(value):
    today_date = timezone.localdate()  # Get today's date
