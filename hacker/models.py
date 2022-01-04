from django.db import models
from default.models import CustomUser
# Create your models here.


class HackerInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="hacker")

    ed_choices = [
        ("High School/Secondary School", "High School/Secondary School"),
        ("University (Undergrad)", "University (Undergrad)"),
        ("University (Master's/Doctoral)", "University (Master's/Doctoral)"),
    ]


    education = models.CharField(max_length=60, null=False, blank=False, choices=ed_choices)
    major = models.CharField(default="other", max_length=60, blank=False, null=False)
    

    class Meta():
        verbose_name = 'Hacker'
    
    def __str__(self):
        return self.hacker.email + ": " + self.hacker.first_name + " " + self.hacker.last_name