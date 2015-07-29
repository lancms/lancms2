# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150729_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='nl1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='slug',
            field=models.SlugField(default='nl1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalorganization',
            name='slug',
            field=models.SlugField(default='nuxis'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(default='nuxis'),
            preserve_default=False,
        ),
    ]
