# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 22, 7, 19, 124954, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 22, 7, 22, 766791, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 22, 7, 31, 759270, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 22, 7, 36, 129190, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
