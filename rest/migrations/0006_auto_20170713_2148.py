# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20170713_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostname',
            name='role_type',
            field=models.ManyToManyField(blank=True, to='rest.Userprofile'),
        ),
    ]
