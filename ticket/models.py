from django.db import models
from core.models import Event
from django.contrib.auth.models import User


# Create your models here.

class TicketType(models.Model):
	Event = models.ForeignKey(Event)
	name = models.CharField(max_length=35)

	def __unicode__(self):
		return self.name


class Ticket(models.Model):
	TicketType = models.ForeignKey(TicketType)
	owner = models.ForeignKey(User)

