from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Profile(models.Model):
    MIN_YEAR = 1984
    MAX_YEAR = 2018
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    MAJOR_CHOICES = (
        ('AUP', 'Architecture & Urban Planning'),
        ('BUS', 'Business'),
        ('LAW', 'Law'),
        ('INF', 'Information'),
        ('LSA', 'Literature, Science, and the Arts'),  
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MinValueValidator(MIN_YEAR), MaxValueValidator(MAX_YEAR)])
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    school = models.CharField(max_length=50,choices=MAJOR_CHOICES)
    location = models.ForeignKey(Location,null=True)