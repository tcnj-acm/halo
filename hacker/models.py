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

    major_hackers = [
        ('Accounting','Accounting'),
        ('Biology', 'Biology'),
        ('Biomedical Engineering', 'Biomedical Engineering'),
        ('Business Administration', 'Business Administration'),
        ('Chemistry','Chemistry'),
        ('Civil Engineering','Civil Engineering'),
        ('Communications','Communications'),
        ('Computer Engineering', 'Computer Engineering'),
        ('Computer Science', 'Computer Science'),
        ('Construction Management', 'Construction Management'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Economics', 'Economics'),
        ('Education', 'Education'),
        ('Electronics Engineering', 'Electronics Engineering'),
        ('English', 'English'), 
        ('Finance', 'Finance'),
        ('Game Design', 'Game Design'),
        ('Health Informatics', 'Health Informatics'),
        ('Industrial Engineering', 'Industrial Engineering'),
        ('Interactive Multimedia', 'Interactive Multimedia'),
        ('Information Technology', 'Information Technology'), 
        ('Liberal Arts', 'Liberal Arts'), 
        ('Management', 'Management'),
        ('Management Information Systems', 'Management Information Systems'), 
        ('Marketing', 'Marketing'), 
        ('Mechanical Engineering', 'Mechanical Engineering'), 
        ('Nuclear Engineering', 'Nuclear Engineering'),
        ('Nursing', 'Nursing'), 
        ('Petroleum Engineering', 'Petroleum Engineering'), 
        ('Physics', 'Physics'), 
        ('Political Science', 'Political Science'), 
        ('Public Administration', 'Public Administration'), 
        ('Software Engineering', 'Software Engineering')
    ]
    education = models.CharField(default="other", max_length=60, null=False, blank=False, choices=ed_choices)
    major = models.CharField(default="other", max_length=60, blank=False,choices=major_hackers)
    

    class Meta():
        verbose_name = 'Hacker'
    
    def __str__(self):
        return self.user.email + ": " + self.user.first_name + " " + self.user.last_name