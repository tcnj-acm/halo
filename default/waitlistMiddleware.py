import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, resolve
from organizer.models import WebsiteSettings
from .helper import decide_redirect, decide_type

class waitlistMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        waitlist = WebsiteSettings.objects.filter(waiting_list_status=True).exists()
        if waitlist:
            print("cool story bro")
        else:
            print("cooler stroy bro")
            try:
                view = reverse('onsomeshit')
                print(view)
            except:
                print('That was on some shit')

        pass

        