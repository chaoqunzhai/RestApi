# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_remove_hostname_role_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostname',
            name='role_type',
            field=models.ManyToManyField(to='rest.Userprofile'),
        ),
    ]
