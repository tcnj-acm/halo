
from django.test import TestCase
from hacker.models import HackerInfo
from default.models import Event
from default.forms import EventCreationForm
from django.core.exceptions import ValidationError

import datetime

#Test the Event creation form using a parametized test
class TestEventForm(TestCase):
    def setUp(self):
        self.fixture_data = (
            (   
                {
                'title':"Long Range Radio Devices",
                'description':"Come and learn about long rnage radio devices",
                'start_time':datetime.time(15,30,0),
                'end_time':datetime.time(16,30,0),
                'date':datetime.date(2021,4,9),
                },
                True
            ),
            (   
                {#title too long
                'title':"Cup Stacking with Ruff Ruffman - On todays episode of cup stacking with ruff ruffman the children will have to run around and gather their own cups from the yard where i have hedden them.",
                'description':"Come compete for cool prizes in the cupstacking event!",
                'start_time':datetime.time(9,0,0),
                'end_time':datetime.time(10,0,0),
                'date':datetime.date(2021,4,10),
                },
                False
            ),
            (   
                {#Not on the hackathon weekend
                'title':"Cup Stacking With the solos",
                'description':"Come and enjoy a fun cupstacking event with the red solos",
                'start_time':datetime.time(9,0,0),
                'end_time':datetime.time(10,0,0),
                'date':datetime.date(2021,4,13),
                },
                False
            ),
            (   
                {
                'title':"Cup Stacking MLH Event",
                'description':"Come compete for cool prizes in the cupstacking event!",
                'start_time':datetime.time(9,0,0),
                'end_time':datetime.time(10,0,0),
                'date':datetime.date(2021,4,10),
                },
                True
            ),
            (   
                { #too early for a saturday event
                'title':"Long Range Radio Devices",
                'description':"Come and learn about long rnage radio devices",
                'start_time':datetime.time(6,30,0),
                'end_time':datetime.time(16,30,0),
                'date':datetime.date(2021,4,9),
                },
                False
            ),
            (   
                { #too late for a sunday event
                'title':"Long Range Radio Devices",
                'description':"Come and learn about long rnage radio devices",
                'start_time':datetime.time(15,30,0),
                'end_time':datetime.time(16,30,0),
                'date':datetime.date(2021,4,10),
                },
                False
            ),
            (   
                { #Description too long
                'title':"Long Range Radio Devices",
                'description':"Come and learn about long rnage radio devices but the evnt will take you forever to actually understand the device so realistically your coming to chill with the gang and have some fun thinking about the applications but never truely being able to implement them unless your that guy but buddy most people are not that guy, definitly not that guy pall",
                'start_time':datetime.time(15,30,0),
                'end_time':datetime.time(16,30,0),
                'date':datetime.date(2021,4,10),
                },
                False
            ),
        )


    def test_event_form_creation(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                form_data = {
                    'title':context["title"],
                    'description':context["description"],
                    'start_time':context["start_time"],
                    'end_time':context["end_time"],
                    'date':context["date"],
                }
                create_event_form = EventCreationForm(data=form_data)
                self.assertEqual(create_event_form.is_valid(), expected)
