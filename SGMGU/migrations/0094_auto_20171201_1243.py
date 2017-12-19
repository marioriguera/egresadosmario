# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-01 17:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0093_auto_20171201_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='existencia',
            name='id_ocupados',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 12, 43, 24, 435000)),
        ),
    ]
