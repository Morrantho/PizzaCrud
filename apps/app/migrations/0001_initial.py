# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('topping1', models.CharField(max_length=255)),
                ('topping2', models.CharField(max_length=255)),
                ('topping3', models.CharField(max_length=255)),
                ('slices', models.IntegerField()),
            ],
        ),
    ]
