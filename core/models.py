### Models
from django.db import models


from django.contrib.auth.models import User
from django_countries import CountryField


CHOICES_GENDER = (
	('female', 'Female'),
	('male', 'Male'),
	)


class UserProfile(models.Model):
	user = models.OneToOneField (User)
	date_of_birth = models.DateField (null=True)
	streetaddress = models.CharField (max_length=255, null=True)
	country = CountryField (null=True)
	postalcode = models.IntegerField (null=True)
	gender = models.CharField (max_length=6, choices=CHOICES_GENDER, null=True)




### Signals

from django.dispatch import receiver
from allauth.account.signals import user_signed_up
import datetime
@receiver(user_signed_up)
def populate_user_profile (request, user, sociallogin=None, **kwargs):
	if sociallogin:
		if sociallogin.account.provider == 'facebook':
			up = UserProfile(user=user)
			up.gender = sociallogin.account.extra_data['gender']
			up.date_of_birth = datetime.datetime.strptime (sociallogin.account.extra_data['birthday'], "%m/%d/%Y")
			up.save()
