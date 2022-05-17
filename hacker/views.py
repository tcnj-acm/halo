from wsgiref.util import request_uri
from django.shortcuts import render, redirect

import hacker
from .models import HackerInfo
from default.forms import CustomUserCreationForm, Event

import hashlib
# Create your views here.

def dash(request):

    hacker = HackerInfo.objects.get(user = request.user)
    first_name_hash = hashlib.sha256(hacker.user.first_name.encode()).hexdigest()
    last_name_hash = hashlib.sha256(hacker.user.last_name.encode()).hexdigest()

    check_in_url = "{}/check-in/{}/{}/{}".format(request.get_host(), first_name_hash,last_name_hash,hacker.user.id)
    context = {'check_in_url':check_in_url, 'hacker':hacker}
    return render(request, 'hackers/dashboard.html', context)

def eventsView(request):
    hacker = HackerInfo.objects.get(user = request.user)
    rsvp_events = Event.objects.exclude(rsvp=hacker)
    non_rsvp_events = Event.objects.filter(rsvp=hacker)
    context = {'rsvp_events':rsvp_events, 'non_rsvp_events':non_rsvp_events}
    return render(request, 'hackers/events.html', context)


def eventRSVP(request, event_id):
    event = Event.objects.get(id = event_id)
    hacker = HackerInfo.objects.get(user = request.user)
    hacker.rsvp_list.add(event)
    return redirect("hacker-events")

def leaveEventRSVP(request, event_id):
    event = Event.objects.get(id = event_id)
    hacker = HackerInfo.objects.get(user = request.user)
    hacker.rsvp_list.remove(event)
    return redirect("hacker-events")
