from django.db import models
from default.models import CustomUser
# Create your models here.
class organizer(models.Model):
    organizer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="organizer")
    address = models.CharField(max_length=60, null=False, blank=False)