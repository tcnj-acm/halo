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
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = str(os.getenv('EM_HOST'))
# EMAIL_PORT = 587
# EMAIL_HOST_USER = str(os.getenv('EM_HOST_USER'))
# EMAIL_HOST_PASSWORD = str(os.getenv('EM_HOST_PASSWORD'))
# EMAIL_USE_TLS=True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR/'static'
]

MEDIA_ROOT = BASE_DIR/'static/images'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
