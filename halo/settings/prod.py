from halo.settings.base import *
from .base import *
import django_heroku
import dj_database_url
import os

load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
DEBUG = False

SECURE_SSL_REDIRECT = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv('DB_NAME')),
        'USER': str(os.getenv('DB_USER')),
        'PASSWORD': str(os.getenv('DB_PASSWORD')),
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': str(os.getenv('DB_PORT')),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'db name',
#         'USER': 'dbuser',
#         'PASSWORD': 'dbpass',
#         'HOST': 'dbhost',
#         'PORT': '5432',
#     }
# }

db_from_env = dj_database_url.config(conn_max_age=1000)
DATABASES['default'].update(db_from_env)

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = str(os.getenv('EM_HOST'))
EMAIL_PORT = 587
EMAIL_HOST_USER = str(os.getenv('EM_HOST_USER'))
EMAIL_HOST_PASSWORD = str(os.getenv('EM_HOST_PASSWORD'))
EMAIL_USE_TLS = True

# AWS S3

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_URL = '/'

STATICFILES_DIRS = [
    BASE_DIR/'static'
]

MEDIA_ROOT = BASE_DIR/'static/images'


AWS_ACCESS_KEY_ID = str(os.getenv('AWS_ACCESS_KEY_ID'))
AWS_SECRET_ACCESS_KEY = str(os.getenv('AWS_SECRET_ACCESS_KEY'))
AWS_STORAGE_BUCKET_NAME = str(os.getenv('AWS_STORAGE_BUCKET_NAME'))
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
