# -*- coding: utf-8

from django.utils.translation import ugettext_lazy as _


### Models
from django.db import models


from django.contrib.auth.models import User, Group
from django_countries.fields import CountryField


CHOICES_GENDER = (
	('female', _('Female')),
	('male', _('Male')),
	)


class UserProfile(models.Model):
	user = models.OneToOneField (User)
	date_of_birth = models.DateField (null=True)
	streetaddress = models.CharField (max_length=255, null=True)
	country = CountryField (null=True)
	postalcode = models.PositiveSmallIntegerField (null=True)
	gender = models.CharField (max_length=6, choices=CHOICES_GENDER, null=True)
	phone = models.CharField (max_length=20, null=True)


	def owns_organizations (self):
		try:
			for group in self.user.groups.all():
				if group.organization_set.filter(is_active=True).count():
					return True
		except:
			return False
	
	def organizations (self):
		try:
			orgs = []
			for group in self.user.groups.all():
				for org in group.organization_set.filter(is_active=True):
					orgs.append (org)
			return orgs
		except:
			pass


class Organization (models.Model):
	name = models.CharField (max_length=64, verbose_name=_('Name'))
	about = models.TextField (null=True, verbose_name=_('About'))
	owner = models.ForeignKey (Group,null=True, verbose_name=_('Owner'))
	is_active = models.BooleanField (default=False)


	def __unicode__ (self):
		return self.name


	class Meta:
		verbose_name = _('Organization')
		verbose_name_plural = _('Organizations')


class Event (models.Model):
	organization = models.ForeignKey(Organization, verbose_name=_('Organization'))
	name = models.CharField (max_length=64, verbose_name=_('Name'))
	owner = models.ForeignKey (Group, verbose_name=_('Owner'))


	def __unicode__ (self):
		return self.name


	class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')
