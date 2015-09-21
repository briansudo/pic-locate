# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landmark',
            name='closest_airport',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='lat',
            field=models.DecimalField(max_digits=8, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='lon',
            field=models.DecimalField(max_digits=8, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='landmark',
            name='summary_url',
            field=models.CharField(max_length=500),
        ),
    ]
