# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=64)),
                ('about', models.TextField(verbose_name='About', null=True)),
                ('is_active', models.BooleanField(verbose_name='Activated', default=False)),
                ('urlslug', models.SlugField(verbose_name='URL-slug', unique=True)),
                ('externalurl', models.URLField(verbose_name='External website', null=True)),
                ('startdatetime', models.DateTimeField(verbose_name='Start time', help_text='YYYY-MM-DD HH:MM')),
                ('enddatetime', models.DateTimeField(verbose_name='End time', help_text='YYYY-MM-DD HH:MM')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=64)),
                ('about', models.TextField(verbose_name='About', null=True)),
                ('is_active', models.BooleanField(verbose_name='Activated', default=False)),
                ('urlslug', models.SlugField(verbose_name='URL-slug', unique=True)),
                ('externalurl', models.URLField(verbose_name='External website', null=True)),
                ('owner', models.ForeignKey(verbose_name='Owner', editable=False, to='auth.Group', null=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_of_birth', models.DateField(null=True)),
                ('streetaddress', models.CharField(max_length=255, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('postalcode', models.PositiveSmallIntegerField(null=True)),
                ('gender', models.CharField(max_length=6, null=True, choices=[('female', 'Female'), ('male', 'Male')])),
                ('phone', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(verbose_name='Organization', editable=False, to='core.Organization'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(verbose_name='Owner', editable=False, to='auth.Group'),
            preserve_default=True,
        ),
    ]
