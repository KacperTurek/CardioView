# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-17 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=250)),
                ('shortcut', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=10)),
                ('shortcut', models.CharField(max_length=10)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sig.Database')),
            ],
        ),
    ]