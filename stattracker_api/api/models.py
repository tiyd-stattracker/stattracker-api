from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    activity_name = models.CharField(max_length=255)
    start_date = models.DateField()
    # activity_date = models.DateField()
    # activity_count = models.PositiveSmallIntegerField()
    # activity_user = models.ForeignKey(User)

class Event(models.Model):
    activity = models.ForeignKey(Activity,related_name='events')
    activity_date = models.DateField()
    activity_count = models.PositiveSmallIntegerField()
