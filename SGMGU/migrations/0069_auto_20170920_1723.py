# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-20 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0068_auto_20170920_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 23, 30, 974000)),
        ),
    ]
