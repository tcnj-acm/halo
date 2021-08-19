from django.db import models
from default.models import CustomUser
# Create your models here.
class organizer(models.Model):
    organizer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="organizer")
    address = models.CharField(max_length=60, null=False, blank=False)


class Setting(models.Model):
    start = models.DateTimeField(auto_now=False, auto_now_add=False)
    end = models.DateTimeField(auto_now=False, auto_now_add=False)