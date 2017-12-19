# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-01 18:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0099_auto_20171201_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 13, 8, 38, 446000)),
        ),
        migrations.AlterField(
            model_name='fluctuacion',
            name='id_fluctuacion',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
