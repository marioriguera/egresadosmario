# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-01 17:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0098_auto_20171201_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 12, 47, 5, 84000)),
        ),
    ]