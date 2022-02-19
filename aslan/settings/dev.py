from aslan.settings.base import *
from .base import *
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EM_HOST = 'localhost'
EM_PORT = 1025
EM_HOST_USER = None
EM_HOST_PASSWORD = None