from django.db import models
from default.models import CustomUser
# Create your models here.


class OrganizerInfo(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="organizer")

    class Meta():
        verbose_name = 'Organizer'

    def __str__(self):
        return self.user.email + ": " + self.user.first_name + " " + self.user.last_name


class WebsiteSettings(models.Model):
    waiting_list_status = models.BooleanField(
        blank=False, choices=[(True, 'Yes'), (False, 'No')])

    class Meta():
        verbose_name = 'Waiting List Setting'

    def __str__(self):
        if self.waiting_list_status:
            return "Waiting List Enabled"
        return "Waiting List Disabled"
