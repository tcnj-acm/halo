# Environmental Variables

You'll need to have 4 different `.env` files for the project.

1. `.env`- located in the base directory of the project
2. `endgrid.env`- located in base directory
3. `.env`- located in the `settings/` folder
4. `creds.env` - located in the `organizer/` app

You can simply create these files in their respective locations, copy the format below for each file, and replace it with your own data.


## .env in base directory

This file stores the credentials for the superuser. 

```env
# Environmental variables for credentials

# Head Organizer Credentials
HEAD_ORG_FIRST_NAME='FIRST'
HEAD_ORG_LAST_NAME='LAST'
HEAD_ORG_EMAIL='mailer@mail.com'
HEAD_ORG_PASSWORD='PASSWORD'
```

## sendgrid.env in base directory

HALO uses Sendgrid for mail relay. This file stores the API key for Sendgrid.

```env
export SENDGRID_API_KEY='API_KEY'
```

Once you have added this in your director be sure to `source ./sendgrid.env` in your shell 


## .env in `settings/` folder

This file stores credentials and other sensitive information for the project settings. Used for both dev mode and production mode. 


```env
# django settings configurations
SECRET_KEY='SECRET'    

# Django allowed hosts 
ALLOWED_HOSTS='["localhost", "127.0.0.1", "YOURDOMAIN"]'


# email credentials
EM_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EM_OUTGOING='mail@mail.com'
EM_HOST='smtp.sendgrid.net'
EM_PORT=NUM
EM_HOST_USER='KEY'
EM_HOST_PASSWORD='PASS'
EM_USE_TLS=True

# AWS S3 Settings

AWS_ACCESS_KEY_ID='KEY_ID'
AWS_SECRET_ACCESS_KEY='ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME='NAME'
DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
```

## creds.env in `organizer/` folder

This file stores the passwords that are used to create organizers or hackers

```env
# Need to add them passwords

# Organizer Passwords
ORGANIZER_PASSWORD='PASS'

# hacker password
HACKER_PASSWORD='PASS'
```
