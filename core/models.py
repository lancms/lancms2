# -*- coding: utf-8

from django.utils.translation import ugettext as _

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



class Organization (models.Model):
	name = models.CharField (max_length=64)
	about = models.TextField (null=True)
	owner = models.ForeignKey (Group)

	def __unicode__ (self):
		return self.name

class Event (models.Model):
	organization = models.ForeignKey(Organization)
	name = models.CharField (max_length=64)
	owner = models.ForeignKey (Group)
	
	def __unicode__ (self):
		return self.name