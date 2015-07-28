from django.db import models

from simple_history.models import HistoricalRecords

from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=256)
    history = HistoricalRecords()


    def __str__(self):
        return self.name


    class Meta:
            permissions = (
                ('manage_organization', 'Can manage organization'),
            )



class Event(models.Model):
    name = models.CharField(max_length=256)
    start = models.DateTimeField()
    end = models.DateTimeField()
    organization = models.ForeignKey(Organization)
    history = HistoricalRecords()


    def __str__(self):
        return self.name


    class Meta:
            permissions = (
                ('manage_event', 'Can manage event'),
            )
