# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Nombre_Ciudad', models.CharField(max_length=70)),
                ('Distrito', models.CharField(max_length=60)),
                ('Poblacion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Lenguaje', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Codigo', models.CharField(max_length=3)),
                ('Nombre', models.CharField(max_length=70)),
                ('Continente', models.CharField(max_length=65)),
                ('Region', models.CharField(max_length=70)),
                ('Area', models.DecimalField(decimal_places=2, max_digits=30)),
                ('Independence', models.IntegerField(default=1500)),
            ],
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='Lenguaje_Pais',
            field=models.ForeignKey(to='Paises.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='Ciudad_pais',
            field=models.ForeignKey(to='Paises.Pais'),
        ),
    ]
