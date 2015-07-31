from django.db import models

from simple_history.models import HistoricalRecords
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from guardian.models import UserObjectPermission
from django.contrib.contenttypes.models import ContentType

class ActiveOrganizationManager(models.Manager):
    def get_queryset(self):
        return super(ActiveOrganizationManager, self).get_queryset().filter(is_active=True)

class ActiveEventManager(models.Manager):
    def get_queryset(self):
        return super(ActiveEventManager, self).get_queryset().filter(is_active=True,organization__is_active=True)

class Organization(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField()

    is_active = models.BooleanField(default=True)

    history = HistoricalRecords()

    objects = ActiveOrganizationManager()


    def get_absolute_url(self):
        return reverse('org_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


    def get_managers(self):
        codename='manage_organization'
        type = ContentType.objects.get_for_model(self)
        return UserObjectPermission.objects.filter(permission__codename=codename, object_pk=self.pk, content_type=type)

    class Meta:
            permissions = (
                ('manage_organization', 'Can manage organization'),
            )



class Event(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField()

    is_active = models.BooleanField(default=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    venuename = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    postalcode = models.CharField(max_length=10)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=256)

    organization = models.ForeignKey(Organization)

    history = HistoricalRecords()

    objects = ActiveEventManager()

    def __str__(self):
        return self.name


    def get_managers(self):
        codename='manage_event'
        type = ContentType.objects.get_for_model(self)
        return UserObjectPermission.objects.filter(permission__codename=codename, object_pk=self.pk, content_type=type)


    class Meta:
            permissions = (
                ('manage_event', 'Can manage event'),
            )
