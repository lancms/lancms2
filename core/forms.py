# -*- coding: utf-8

from django.utils.translation import ugettext as _

### Forms
from django import forms
from django.forms.extras.widgets import SelectDateWidget
import datetime
from core.models import UserProfile, CHOICES_GENDER

class SignupForm (forms.Form):
	# FIXME: Not sure if hardcoding a copy of the d.c.auth.m.User and core.models.UserProfile is the right thing to do, but I'll do it for now:
	first_name = forms.CharField (max_length=30, label=_('First name'))
	last_name = forms.CharField (max_length=30, label=_('Last name'))
	date_of_birth = forms.DateField (widget=SelectDateWidget(years=range(datetime.date.today().year, 1900, -1)), label=_('Date of birth'))
	streetaddress = forms.CharField (max_length=255, label=_('Street address'))
	postalcode = forms.IntegerField (label=_('Postal code'))
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
		userprofile.save ()
	
	def __init__ (self, *args, **kwargs):
		sociallogin = self.sociallogin
		initial = kwargs['initial']
		initial['date_of_birth'] = datetime.datetime.strptime(sociallogin.account.extra_data['birthday'], "%m/%d/%Y")
		initial['gender'] = sociallogin.account.extra_data['gender']
		# mboehn: This is some interesting stuff. What am I doing???!
		kwargs.update (
			{ 'initial': initial,
			}
		)
		super (SignupForm, self).__init__ (*args, **kwargs)
