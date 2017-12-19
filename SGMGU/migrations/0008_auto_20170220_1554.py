# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 20:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0007_auto_20170220_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 54, 29, 460000)),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 54, 29, 464000)),
        ),
        migrations.AlterField(
            model_name='expediente_no_aprobado',
            name='fecha_no_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 54, 29, 464000)),
        ),
        migrations.AlterField(
            model_name='expediente_pendiente',
            name='fecha_pendiente',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 54, 29, 463000)),
        ),
        migrations.AlterField(
            model_name='expediente_rechazado',
            name='fecha_rechazo',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 15, 54, 29, 462000)),
        ),
    ]
