# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-01 17:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0088_auto_20171115_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 1, 12, 7, 49, 652000)),
        ),
    ]