# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaje.Destino')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaje.Destino')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('excursion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaje.Excursion')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaje.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200)),
                ('correoElectronico', models.EmailField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaYFechaDeEmbarque', models.DateTimeField()),
                ('precio', models.FloatField()),
                ('nombreDeVuelo', models.CharField(max_length=200)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaje.Destino')),
            ],
        ),
        migrations.AddField(
            model_name='paquete',
            name='vuelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viaje.Vuelo'),
        ),
    ]
