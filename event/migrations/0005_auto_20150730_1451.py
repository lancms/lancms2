# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20150730_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venuename',
            field=models.CharField(max_length=256, default='Storhallen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='venuename',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
    ]
