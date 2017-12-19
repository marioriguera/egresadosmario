# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-20 21:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGMGU', '0067_auto_20170907_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id_codigo_entidad', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('e_nombre', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('municipio', models.IntegerField(blank=True, null=True)),
                ('id_tipo', models.IntegerField(blank=True, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('est_replica', models.IntegerField(blank=True, null=True)),
                ('id_organismo_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SGMGU.Organismo')),
            ],
        ),
        migrations.AlterField(
            model_name='expediente_aprobado',
            name='fecha_aprobado',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 17, 4, 15, 615000)),
        ),
    ]
