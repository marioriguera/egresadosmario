# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2008-04-30 08:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0025_auto_20080430_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubicacionlaboral',
            name='presentado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2008, 4, 30, 4, 3, 38, 718000)),
        ),
    ]
