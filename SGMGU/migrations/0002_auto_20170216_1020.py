# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 15:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='causal_movimiento',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='centro_estudio',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 16, 10, 20, 32, 538000)),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 16, 10, 20, 32, 543000)),
        ),
        migrations.AlterField(
            model_name='expediente_no_aprobado',
            name='fecha_no_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 16, 10, 20, 32, 544000)),
        ),
        migrations.AlterField(
            model_name='expediente_pendiente',
            name='fecha_pendiente',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 16, 10, 20, 32, 542000)),
        ),
        migrations.AlterField(
            model_name='expediente_rechazado',
            name='fecha_rechazo',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 16, 10, 20, 32, 541000)),
        ),
    ]