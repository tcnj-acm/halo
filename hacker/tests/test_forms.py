from django.test import TestCase
from hacker.models import HackerInfo
from default.models import Event
from default.forms import EventCreationForm

import datetime

class TestEventForm(TestCase):

    def test_event_form_success(self):
        form_data = {
            'title':"Long Range Radio Devices",
            'description':"Come and learn about long rnage radio devices",
            'start_time':datetime.time(15,30,0),
            'end_time':datetime.time(16,30,0),
            'date':datetime.date(2021,4,9),
        }

        create_event_form = EventCreationForm(data=form_data)
        
        self.assertTrue(create_event_form.is_valid())