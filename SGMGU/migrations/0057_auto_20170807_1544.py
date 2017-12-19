# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-07 19:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0056_auto_20170807_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 15, 44, 38, 764000)),
        ),
        migrations.AlterField(
            model_name='procesoinhabilitacion',
            name='causal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SGMGU.Causal_movimiento'),
        ),
    ]
