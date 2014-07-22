from django.db import models

from django.utils.translation import ugettext_lazy as _


# Import models from other apps
from core.models import Event, User

# Create your models here.
CHOICES_TICKETTYPES = (
	('prepaid', _('Prepaid')),
	('preorder', _('Preordered')),
	)
class TicketType(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=64, verbose_name=_('Name'))
	type = models.CharField (max_length=10, choices=CHOICES_TICKETTYPES)
	
	def __unicode__ (self):
		return self.name

	class Meta:
		verbose_name = _('Tickettype')
		verbose_name_plural = _('Tickettypes')