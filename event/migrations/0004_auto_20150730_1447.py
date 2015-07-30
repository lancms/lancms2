# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20150729_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(max_length=256, default='Storgata 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=64, default='Tønsberg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(max_length=256, default='Norway'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='postalcode',
            field=models.CharField(max_length=10, default='3120'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='address',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='city',
            field=models.CharField(max_length=64, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='country',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalevent',
            name='postalcode',
            field=models.CharField(max_length=10, default=''),
            preserve_default=False,
        ),
    ]
