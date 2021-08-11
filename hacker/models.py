from django.db import models
from default.models import CustomUser
# Create your models here.


class hacker(models.Model):
    hacker = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="hacker")

    ed_choices = [
        ("High School/Secondary School", "High School/Secondary School"),
        ("University (Undergrad)", "University (Undergrad)"),
        ("University (Master's/Doctoral)", "University (Master's/Doctoral)"),
    ]

    food_choices = [
        ("None", "None"),
        ("Vegetarian", "Vegetarian"),
        ("Vegan", "Vegan"),
        ("Gluten-Free", "Gluten-Free")
    ]

    size_choices = [
        ("Unisex (XS)", "Unisex (XS)"),
        ("Unisex (S)", "Unisex (S)"),
        ("Unisex (M)", "Unisex (M)"),
        ("Unisex (L)", "Unisex (L)"),
        ("Unisex (2XL)", "Unisex (2XL)"),
        ("Unisex (3XL)", "Unisex (3XL)")
    ]
    address = models.CharField(max_length=60, null=False, blank=False)
    education = models.CharField(max_length=60, null=False, blank=False, choices=ed_choices)
    major = models.CharField(default="other", max_length=60, blank=False, null=False)
    food_preference = models.CharField(default="None", max_length=20, blank=False, null=False, choices=food_choices)
    shirt_size = models.CharField(default="Unisex (M)", max_length=20, blank=False, null=False, choices=size_choices)