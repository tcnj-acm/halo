from django.test import TestCase
from hacker.models import HackerInfo
from default.models import Event, CustomUser
from default.helper import add_group
from django.contrib.auth.models import Group
from django.urls import reverse
import random, datetime

class TestEventViews(TestCase):
    def setUp(self):
        Group.objects.create(name="hacker") #Set up for creating hackers

        testUser = CustomUser.objects.create(email="kevin@halo.com", first_name="Kevin", last_name="Williams",address="12 Xbox Lane", food_preference="None", shirt_size="Unisex (M)", age=random.randint(14,22)) #create user
        testUser.set_password("r4nd0m_p455w0rd*")
        testUser.save()
        add_group(testUser, "hacker")
        hacker = HackerInfo.objects.create(user=testUser)

        #Create Three Events to work with during the integration testing
        self.testEvent1 = Event.objects.create(title="Cup Stacking", description="Come compete for cool prizes in the cupstacking event!", start_time=datetime.time(10,30,0), end_time=datetime.time(11,30,0), date=datetime.date(2021, 4, 9) )
        self.testEvent2 = Event.objects.create(title="Long Range Radio Devices", description="Come and learn about long rnage radio devices", start_time=datetime.time(15,30,0), end_time=datetime.time(16,30,0), date=datetime.date(2021,4,9) )
        self.testEvent3 = Event.objects.create(title="Git Hub Workshop", description="Come and learn about git hub", start_time=datetime.time(22,30,0), end_time=datetime.time(23,30,0), date=datetime.date(2021,4,9) )
    
    #Test to ensure that only logged in users can view the rsvp site
    def test_events_view_non_logged_in(self):
        response = self.client.get(reverse('hacker-events'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url == "/")

    #Logging in user and then testing to ensure all events are visible on the events page
    def test_events_view_logged_in(self):
        login = self.client.login(email="kevin@halo.com", password="r4nd0m_p455w0rd*")
        response = self.client.get(reverse('hacker-events')) #send get request to event page

        self.assertTrue('rsvp_events' and 'non_rsvp_events' in response.context) #Ensure view is querying and sending correct data

        self.assertEquals(len(response.context['rsvp_events']), 3) #Ensure that at this stage 3 events are available to rsvp (the ones created during set up)
        self.assertEquals(len(response.context['non_rsvp_events']), 0) #ENo events have been rsvp'd by this user yet


    #Logging in and testing to ensure that users can rsvp
    def test_events_rsvp_view(self):
        login = self.client.login(email="kevin@halo.com", password="r4nd0m_p455w0rd*")

        response = self.client.get(reverse("hacker-rsvp", kwargs={'event_id':self.testEvent2.pk,})) #Sends get request with pk of event to be rsvp'd by user

        response = self.client.get(reverse('hacker-events')) #go back to event view page

        #Ensure that the number available has gone down and that the number rsvp'd for has gone up
        self.assertTrue('rsvp_events' and 'non_rsvp_events' in response.context)
        self.assertEquals(len(response.context['rsvp_events']), 2)
        self.assertEquals(len(response.context['non_rsvp_events']), 1)

        #Send another request to rsvp
        response = self.client.get(reverse("hacker-rsvp", kwargs={'event_id':self.testEvent1.pk,}))
        response = self.client.get(reverse('hacker-events'))

        #Ensure that the number available has gone down and that the number rsvp'd for has gone up
        self.assertTrue('rsvp_events' and 'non_rsvp_events' in response.context)
        self.assertEquals(len(response.context['rsvp_events']), 1)
        self.assertEquals(len(response.context['non_rsvp_events']), 2)

    #Logging in and testing that users can un-rsvp
    def test_events_release_rsvp_view(self):
        login = self.client.login(email="kevin@halo.com", password="r4nd0m_p455w0rd*")

        #RSVP for all events as starting point
        response = self.client.get(reverse("hacker-rsvp", kwargs={'event_id':self.testEvent3.pk,}))
        response = self.client.get(reverse("hacker-rsvp", kwargs={'event_id':self.testEvent2.pk,}))
        response = self.client.get(reverse("hacker-rsvp", kwargs={'event_id':self.testEvent1.pk,}))
        response = self.client.get(reverse('hacker-events'))

        #Ensure all have been added
        self.assertTrue('rsvp_events' and 'non_rsvp_events' in response.context)
        self.assertEquals(len(response.context['rsvp_events']), 0)
        self.assertEquals(len(response.context['non_rsvp_events']), 3)

        #send request to remove
        response = self.client.get(reverse("hacker-unrsvp", kwargs={'event_id':self.testEvent3.pk,}))
        response = self.client.get(reverse('hacker-events'))

        #ensure that rsvp'd goes down and available goes up
        self.assertTrue('rsvp_events' and 'non_rsvp_events' in response.context)
        self.assertEquals(len(response.context['rsvp_events']), 1)
        self.assertEquals(len(response.context['non_rsvp_events']), 2)

        #Test once more 
        response = self.client.get(reverse("hacker-unrsvp", kwargs={'event_id':self.testEvent2.pk,}))
        response = self.client.get(reverse('hacker-events'))

        self.assertTrue('rsvp_events' and 'non_rsvp_events' in response.context)
        self.assertEquals(len(response.context['rsvp_events']), 2)
        self.assertEquals(len(response.context['non_rsvp_events']), 1)
        

