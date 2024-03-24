from django.core.exceptions import ValidationError
from django.utils import timezone
import re


def validate_future_date(value):
