from django.db import models
from core.models import Event
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy as _

# Create your models here.

class TicketType(models.Model):
	Event = models.ForeignKey(Event)
	Name = models.CharField(max_length=35)
	ValidSoldFrom = models.DateTimeField(blank=True)
	ValidSoldUntil = models.DateTimeField(blank=True)
	TypeChoice = (
		('onsite-noncomputer', 'Onsite: Without computer'),
		('onsite-withcomputer', 'Onsite: With computer'),
		('prepaid', 'Prepaid'),
		('preorder', 'Preorder'),
		('special-crew', 'Crew'),
		('special-invitation', 'Special invitation'),
	)
	Type = models.CharField(max_length=15, choices=TypeChoice)
#	Type = models.CharField(max_length=15)

	def __unicode__(self):
		return self.name


class Ticket(models.Model):
	TicketType = models.ForeignKey(TicketType)
	owner = models.ForeignKey(User)

