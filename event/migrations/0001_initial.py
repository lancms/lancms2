# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'permissions': (('manage_event', 'Can manage event'),),
            },
        ),
        migrations.CreateModel(
            name='HistoricalEvent',
            fields=[
                ('id', models.IntegerField(blank=True, auto_created=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, related_name='+', to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical event',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalOrganization',
            fields=[
                ('id', models.IntegerField(blank=True, auto_created=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, related_name='+', to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical organization',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'permissions': (('manage_organization', 'Can manage organization'),),
            },
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='organization',
            field=models.ForeignKey(null=True, related_name='+', db_constraint=False, blank=True, to='event.Organization', on_delete=django.db.models.deletion.DO_NOTHING),
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(to='event.Organization'),
        ),
    ]
