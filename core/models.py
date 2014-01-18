# -*- coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

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
	is_active = models.BooleanField (default=False, verbose_name=_('Activated'))
	urlslug = models.SlugField (unique=True, verbose_name=_('URL-slug'))
	externalurl = models.URLField (null=True, verbose_name=_('External website'))


	def __unicode__ (self):
		return self.name


	def user_is_owner (self, user):
		# FIXME: could I have dropped pk? Not sure what else to filter on... -- mboehn
		return user.groups.filter(pk=self.owner.pk).exists()


	def owners (self):
		return self.owner.user_set.filter(is_active=True)


	def events (self):
		# shows all events, so that org owners can activate/deactivate?
		return self.event_set.all ()

	
	def get_absolute_url (self):
		return reverse ('organization_front', args=[self.urlslug])
	

	class Meta:
		verbose_name = _('Organization')
		verbose_name_plural = _('Organizations')


class Event (models.Model):
	organization = models.ForeignKey(Organization, verbose_name=_('Organization'))
	name = models.CharField (max_length=64, verbose_name=_('Name'))
	owner = models.ForeignKey (Group, verbose_name=_('Owner'))
	is_active = models.BooleanField (default=False, verbose_name=_('Activated'))
	urlslug = models.SlugField (unique=True, verbose_name=_('URL-slug'))
	externalurl = models.URLField (null=True, verbose_name=_('External website'))
	startdatetime = models.DateTimeField(verbose_name=_('Start time'), help_text='YYYY-MM-DD HH:MM') # FIXME: help_text should be replaced by using a proper datetime widget for this
	enddatetime = models.DateTimeField(verbose_name=_('End time'), help_text='YYYY-MM-DD HH:MM') # FIXME: help_text should be replaced by using a proper datetime widget for this


	def __unicode__ (self):
		return self.name


	class Meta:
		verbose_name = _('Event')
		verbose_name_plural = _('Events')
