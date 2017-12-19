# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-28 16:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0021_auto_20170620_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='codigo_DE_RS',
            field=models.CharField(blank=True, max_length=250, null=True, unique_for_year=True),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 12, 11, 14, 222000)),
        ),
    ]