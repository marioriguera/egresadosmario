# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-01 17:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0095_auto_20171201_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='existencia',
            name='id_ocupados',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 12, 44, 41, 706000)),
        ),
    ]
