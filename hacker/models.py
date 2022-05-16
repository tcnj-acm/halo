from django.db import models
from default.models import CustomUser, Event
# Create your models here.


class HackerInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="hacker")
    rsvp_list = models.ManyToManyField(Event, related_name="rsvp")

    class Meta():
        verbose_name = 'Hacker'
    
    def __str__(self):
        return self.user.email + ": " + self.user.first_name + " " + self.user.last_name