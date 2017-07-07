# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20170615_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitados', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='Tipo',
            new_name='tipo',
        ),
        migrations.AddField(
            model_name='boda',
            name='catering',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Catering'),
        ),
        migrations.AddField(
            model_name='boda',
            name='tematica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Tematica'),
        ),
    ]
