# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0062_auto_20170809_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandagraduados',
            name='municipio_entidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 9, 15, 45, 34, 6000)),
        ),
    ]
