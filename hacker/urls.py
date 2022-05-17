from django.urls import path, re_path
from hacker import views 

urlpatterns = [

    path('hdash', views.dash, name='hacker-dash'),
    path('hackers/events', views.eventsView, name='hacker-events'),
    path('hackers/events/add/<int:event_id>', views.eventRSVP, name='hacker-rsvp'),
    path('hackers/events/remove/<int:event_id>', views.leaveEventRSVP, name='hacker-unrsvp'),

]