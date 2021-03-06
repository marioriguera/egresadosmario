# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 18:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0009_auto_20170307_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='fecha_registro',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 17, 14, 52, 24, 496000)),
        ),
        migrations.AlterField(
            model_name='expediente_no_aprobado',
            name='fecha_no_aprobado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expediente_pendiente',
            name='fecha_pendiente',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expediente_rechazado',
            name='fecha_rechazo',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
