from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
    activity_name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    user = models.ForeignKey(User, related_name='activities')



    def __str__(self):
        return self.activity_name


class Log(models.Model):
    activity = models.ForeignKey(Activity,related_name='logs')
    activity_date = models.DateField()
    activity_count = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['-activity_date']
        unique_together = ('activity', 'activity_date')
