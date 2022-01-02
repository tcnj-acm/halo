from django.db import models
from default.models import CustomUser
# Create your models here.
class organizer(models.Model):
    organizer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="organizer")
    address = models.CharField(max_length=60, null=False, blank=False)

    class Meta():
        verbose_name = 'Organizer'
    
    def __str__(self):
        return self.organizer.email + ": " + self.organizer.first_name + " " + self.organizer.last_name



class WaitingListControl(models.Model):
    waiting_list_status = models.BooleanField(blank=False, choices = [(True, 'Yes'), (False, 'No')])

    class Meta():
        verbose_name = 'Waiting List Setting'
    
    def __str__(self):
        if self.waiting_list_status:
            return "Waiting List Enabled"
        return "Waiting List Disabled"


class WaitingListSupervisors(models.Model):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)

    class Meta():
        verbose_name = 'Waiting List Supervisor'
    
    def __str__(self):
        return self.email
