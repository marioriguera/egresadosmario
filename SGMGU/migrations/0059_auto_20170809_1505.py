# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 19:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0058_auto_20170808_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demandagraduados',
            options={},
        ),
        migrations.RemoveField(
            model_name='demandagraduados',
            name='activo',
        ),
        migrations.RemoveField(
            model_name='demandagraduados',
            name='fecha_registro',
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_cinco',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_cuatro',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_diez',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_dos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_nueve',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_ocho',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_seis',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_siete',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_tres',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='anno_mas_uno',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demandagraduados',
            name='nombre_entidad',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 9, 15, 5, 40, 978000)),
        ),
    ]