# -*- coding: utf-8

import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext as _
from django.contrib.auth.models import Group, User
from django.contrib import messages

from django_countries import countries

from core.models import Event
from core.models import UserProfile, CHOICES_GENDER



class SignupForm (forms.Form):
	# FIXME: Not sure if hardcoding a copy of the d.c.auth.m.User and core.models.UserProfile is the right thing to do, but I'll do it for now:
	first_name = forms.CharField (max_length=30, label=_('First name'))
	last_name = forms.CharField (max_length=30, label=_('Last name'))
	date_of_birth = forms.DateField (widget=SelectDateWidget(years=range(datetime.date.today().year, 1900, -1)), label=_('Date of birth'))
	streetaddress = forms.CharField (max_length=255, label=_('Street address'))
	postalcode = forms.IntegerField (label=_('Postal code'))
	country = forms.ChoiceField (choices=countries, label=_('Country'))
	gender = forms.ChoiceField (choices=CHOICES_GENDER, label=_('Gender'))
	phone = forms.CharField (max_length=20, label=_('Phone'))

	def save (self, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save ()
		userprofile, upcreated = UserProfile.objects.get_or_create (user=user)
		userprofile.date_of_birth = self.cleaned_data['date_of_birth']
		userprofile.streetaddress = self.cleaned_data['streetaddress']
		userprofile.postalcode = self.cleaned_data['postalcode']
		userprofile.gender = self.cleaned_data['gender']
		userprofile.phone = self.cleaned_data['phone']
		userprofile.country = self.cleaned_data['country']
		userprofile.save ()
	
	def __init__ (self, *args, **kwargs):
		try:
			sociallogin = self.sociallogin
			initial = kwargs['initial']
			initial['date_of_birth'] = datetime.datetime.strptime(sociallogin.account.extra_data['birthday'], "%m/%d/%Y")
			initial['gender'] = sociallogin.account.extra_data['gender']
			# mboehn: This is some interesting stuff. What am I doing???!
			kwargs.update (
				{ 'initial': initial,
				}
			)
		except:
			pass


		super (SignupForm, self).__init__ (*args, **kwargs)


class EventForm (forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'about', 'urlslug', 'externalurl', 'startdatetime', 'enddatetime']
	
	def save (self, org, *args, **kwargs):
		group = Group(name='event_' + self.instance.urlslug + '_owners')
		group.save ()

		self.instance.organization = org
		self.instance.owner = group

		post = super (EventForm, self).save (*args, **kwargs)
		post.save()


class EventOwnerAddForm (forms.Form):
	username = forms.CharField (max_length=30, label=_('Username'))
	
	
	def user_exists (self):
		try:
			print (self.cleaned_data['username'])
			user = User.objects.get(username=self.cleaned_data['username'])
			return True
		except:
			return False


	def user_is_new (self, event):
		user = User.objects.get(username=self.cleaned_data['username'])
		if user.groups.filter(name=event.owner.name).exists():
			# FIXME: not sure if I should return redirect from here or if should return to the view before doing that. -- mboehn
			return False
		else:
			return True


	def save (self, event):
		user = User.objects.get(username=self.cleaned_data['username'])
		event.owner.user_set.add (user)

class EventSetting (forms.ModelForm):
	class Meta:
		model = Event
#		fields = ['name', 'about', 'is_active', 'externalurl', 'startdatetime', 'enddatetime']
#		exclude = ('owner_id', 'organization_id',)

	def save (self, event, *args, **kwargs):

#		self.instance.organization = self.organization
#		self.instance.owner = model.owner
		post = super (EventSetting, self).save (*args, **kwargs)
#		post.organization = event.organization
		post.save()
