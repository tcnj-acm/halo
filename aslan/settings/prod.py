from aslan.settings.base import *
from .base import *
import django_heroku
import dj_database_url
import os 

SECRET_KEY = str(os.getenv('SECRET_KEY'))
DEBUG = True


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': str(os.getenv('DB_NAME')),
#         'USER': str(os.getenv('DB_USER')),
#         'PASSWORD': str(os.getenv('DB_PASSWORD')),
#         'HOST': str(os.getenv('DB_HOST')),
#         'PORT': str(os.getenv('DB_PORT')),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db name',
        'USER': 'dbuser',
        'PASSWORD': 'dbpass',
        'HOST': 'dbhost',
        'PORT': '5432',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EM_HOST')
EMAIL_PORT = os.getenv('EM_PORT')
EMAIL_HOST_USER = os.getenv('EM_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EM_HOST_PASSWORD')
EMAIL_USE_TLS=os.getenv('EM_USE_TLS')

# AWS S3
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = os.getenv('AWS_S3_FILE_OVERWRITE')
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

django_heroku.settings(locals(), test_runner=False)