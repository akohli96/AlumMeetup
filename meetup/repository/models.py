from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import migrations, models
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

    def __unicode__ (self):
        return '<User %s>' % self.user.username

    def gender_verbose(self):
        return dict(Profile.GENDER_CHOICES)[self.gender]

    def school_verbose(self):
        return dict(Profile.MAJOR_CHOICES)[self.school]

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Event(models.Model):
    public = models.BooleanField(default=True)
    location = models.ManyToManyField(Location) #by default location of jost
    host = models.ManyToManyField(Profile, related_name='host_profile')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest = models.ManyToManyField(Profile) #host always part of list

    date = models.DateField(default=timezone.now)
    modified = AutoDateTimeField(default=timezone.now)