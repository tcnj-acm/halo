import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, resolve
from .helper import decide_redirect, decide_type
from pprint import pprint
from organizer.models import OrganizerInfo, WebsiteSettings, FeaturePermission, OrganizerPermission


class OrganizerFeatureMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        if decide_type(request.user) != 'organizer':
            return None

        path = request.path_info
        url_name = resolve(path).url_name
        permisson = FeaturePermission.objects.filter(url_name=url_name)
        
        if not permisson.exists():
            return None
        
        if permisson.first().organizer_permission.filter(user=request.user).exists():
            pass
        else:
            return redirect('organizer-dash')

