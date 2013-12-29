from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Event(models.Model):
	name = models.CharField(max_length=64)

	class Meta:
		permissions = (
			("add", "Add"),
			("change", "Change"),
		)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField ()
	postnumber = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	cellphone = models.CharField(max_length=10)
	facebookID = models.IntegerField(max_length=15,blank=True)
	registerIP = models.GenericIPAddressField()
	profilePicture = models.FileField(upload_to='profilePicture/', blank=True)
