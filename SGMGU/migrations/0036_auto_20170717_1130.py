# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-17 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0035_auto_20170717_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 17, 11, 30, 30, 245000)),
        ),
        migrations.AlterField(
            model_name='ubicacionlaboral',
            name='boleta',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
