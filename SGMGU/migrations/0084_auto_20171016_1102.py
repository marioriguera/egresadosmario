# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-16 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0083_auto_20170929_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 11, 2, 9, 247000)),
        ),
    ]
