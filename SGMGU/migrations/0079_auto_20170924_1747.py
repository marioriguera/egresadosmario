# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-24 23:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0078_auto_20170924_1622'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_entidad',
            options={'ordering': ['nombre_tipo']},
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 17, 47, 59, 91000)),
        ),
    ]
