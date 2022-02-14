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
        verbose_name = 'Website Settings'

    def __str__(self):
        if self.waiting_list_status:
            return "Waiting List Enabled"
        return "Waiting List Disabled"


class FeaturePermission(models.Model):
    url_name = models.CharField(max_length=100, blank=False, null=False)
    permission_name = models.CharField(max_length=100, blank=False, null=False)

    class Meta():
        verbose_name = 'Feature Permission'

    def __str__(self):
        return self.permission_name


class OrganizerPermission(models.Model):
    permission = models.ManyToManyField(
        FeaturePermission, related_name='organizer_permission')
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='user')

    class Meta():
        verbose_name = 'Organizer Permissions'

    def __str__(self):
        return f"{self.user.first_name} of {[permission for permission in self.permission.all()]}" 
