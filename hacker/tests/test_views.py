from django.test import TestCase
from hacker.models import HackerInfo
from default.models import Event
from default.forms import EventCreationForm
from django.core.exceptions import ValidationError