from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.
from core.models import Event, User

class Crew(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=64, verbose_name=_('Name'))
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Crew')
		verbose_name_plural = _('Crews')


class CrewMembers(models.Model):
	user = models.ForeignKey(User)
	crew = models.ForeignKey(Crew)
	access = models.IntegerField(max_length=1, verbose_name=_('Access'))

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('CrewMembers')
		verbose_name_plural = _('CrewMembers')
