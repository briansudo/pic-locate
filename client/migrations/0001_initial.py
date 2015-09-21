# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import client.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('summary_url', models.CharField(max_length=100)),
                ('closest_airport', models.IntegerField()),
                ('classification_id', models.IntegerField()),
                ('lat', models.DecimalField(max_digits=7, decimal_places=3)),
                ('lon', models.DecimalField(max_digits=7, decimal_places=3)),
                ('image', models.ImageField(null=True, upload_to=client.models.get_image_path, blank=True)),
            ],
        ),
    ]
