# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 20:06
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0039_auto_20170802_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 2, 16, 6, 1, 569000)),
        ),
        migrations.AlterField(
            model_name='graduadoinhabilitacion',
            name='ci',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message=b'CI incorrecto', regex=b'^[0-9]{2}(0[1-9]|1[0-2])(31|30|(0[1-9]|[1-2][0-9]))[0-9]{5}$')]),
        ),
    ]
