import re
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from .helper import decide_redirect, decide_type

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS = [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


"""
The exempt URLS for each type. This will allow them to 
bypass in certain specific scenarios.
"""
ALL_EXEMPT_URLS = { #URLS that anyone should be able to access outside of their views

}

hacker_exempt_URLS = { #Any urls outside of hacker.views that they can access

}

organizer_exempt_URLS = { #Any urls outside of organizer.views that they can access

}

not_organizer_exempt_URLS = { #Any urls inside of organizer.views that regular Organizers can not access

}

haed_organizer_exempt_URLS = { #Any urls outside of organizer.views that head can access can access
    
}

# sponsor_exempt_URLS = { #Any urls outside of sponsors.views that they can access
# 
# }


"""
The modules for each type. Grants acces for a type to  
view every page in their module.
"""

hacker_mods = {
    "hacker.views",
}
organizer_mods = {
    "organizer.views",
}
head_organizer_mods = {
    "organizer.views",
}
# sponsor_mods = {
#     "hacker.views",
# }

HACKER_EXEMPT_URLS = [re.compile(url) for url in hacker_exempt_URLS]
ORGANIZER_EXEMPT_URLS = [re.compile(url) for url in organizer_exempt_URLS]
NOT_ORGANIZER_EXEMPT_URLS = [re.compile(url) for url in not_organizer_exempt_URLS]
HEAD_ORGANIZER_EXEMPT_URLS = [re.compile(url) for url in haed_organizer_exempt_URLS]
# SPONSOR_EXEMPT_URLS = [re.compile(url) for url in sponsor_exempt_URLS]



class loginMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request,'user')
        path = request.path_info.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(decide_redirect(request.user))
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect('login')



class accountsMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
   

    def process_view(self, request, view_func, view_args, view_kwargs):
        module_name = view_func.__module__
        user = request.user
        path = request.path_info.lstrip('/')

        if path == 'logout/':
            return None

        if any(url.match(path) for url in ALL_EXEMPT_URLS):
            return None

        user_type = decide_type(user)

        if user_type == 'hacker':
            if any(mod == module_name for mod in hacker_mods):
                pass
            elif any(url.match(path) for url in HACKER_EXEMPT_URLS):
                pass
            else:
                return redirect('hacker-dash')
        elif user_type == 'organizer':
            if any(mod == module_name for mod in organizer_mods):
                if any(url.match(path) for url in NOT_ORGANIZER_EXEMPT_URLS):
                    return redirect(user_type)
                pass
            elif any(url.match(path) for url in ORGANIZER_EXEMPT_URLS):
                pass
            else:
                return redirect('organizer_dash')
        else: #head organizer
            if any(mod == module_name for mod in head_organizer_mods):
                pass
            elif any(url.match(path) for url in HEAD_ORGANIZER_EXEMPT_URLS): 
                pass
            else:
                return redirect('organizer_dash')