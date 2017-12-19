# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 18:40
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0020_auto_20170615_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 14, 40, 5, 979000)),
        ),
        migrations.AlterField(
            model_name='ubicacionlaboral',
            name='boleta',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ubicacionlaboral',
            name='ci',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(message=b'CI incorrecto', regex=b'^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$')]),
        ),
    ]