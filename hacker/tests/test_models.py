from django.test import TestCase
from hacker.models import HackerInfo
from default.models import Event
from django.core.exceptions import ObjectDoesNotExist

import datetime

#Test the model creation and deletion
class EventModelTest(TestCase):
    
    def create_event(self, title, description, start, end, date):
        return Event.objects.create(title=title, description=description, start_time=start, end_time=end, date=date)

    def test_event_creation(self):
        event = self.create_event("Cup Stacking", "Come compete for cool prizes in the cupstacking event!", datetime.time(10,30,0), datetime.time(11,30,0), datetime.date(2021, 4, 9) )
        self.assertTrue(isinstance(event, Event))
        eventObj = Event.objects.get(title="Cup Stacking")
        self.assertEqual(str(event), str(eventObj))

    def test_event_deletion(self):
        self.create_event("Cup Stacking", "Come compete for cool prizes in the cupstacking event!", datetime.time(10,30,0), datetime.time(11,30,0), datetime.date(2021, 4, 9) )
        eventObj = Event.objects.get(title="Cup Stacking")
        eventObj.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Event.objects.get(title="Cup Stacking") #calls an exception if not found


