from atexit import register
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,  PermissionsMixin
from django.core.validators import MaxValueValidator
from .managers import CustomUserManager
from .choices import *
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):


    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200, null=False, blank=True)
    food_preference = models.CharField(default="None", max_length=20, blank=False, null=False, choices=food_choices)
    shirt_size = models.CharField(default="Unisex (M)", max_length=20, blank=False, null=False, choices=size_choices)
    gender = models.CharField(default="Prefer not to say", max_length=20, blank=False,null=False, choices=gender_choices)
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(125)])
    school_name = models.CharField(default="",max_length=75, null=False, blank=False)
    level_of_study = models.CharField(default="University (Undergrad)", max_length=60, null=False, blank=False, choices=los_choices)
    major = models.CharField(default="other", max_length=60, blank=False,choices=major_hackers)
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    registration_comment = models.TextField(null=True, blank=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Event(models.Model):

    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField()

    def __str__(self):
        return self.title + str(self.date) + str(self.start_time) + '-' + str(self.end_time)


class WaitingList(models.Model):

    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    full_name = models.CharField(max_length=64)

    def __str__(self):
        return self.email + ": " + self.full_name