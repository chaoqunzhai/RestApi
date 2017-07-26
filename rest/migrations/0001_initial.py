# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('disk', models.CharField(blank=True, max_length=8, null=True)),
                ('cpu', models.CharField(blank=True, max_length=8, null=True)),
                ('kernel', models.CharField(blank=True, max_length=24, null=True)),
                ('source', models.SmallIntegerField(choices=[(0, 'B28'), (1, 'B2C'), (2, '大数据'), (3, '开发测试'), (4, '运维开发')])),
            ],
            options={
                'verbose_name_plural': '主机',
            },
        ),
        migrations.CreateModel(
            name='Saltrun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun', models.CharField(max_length=16, verbose_name='SALT模块')),
                ('fun_args', models.CharField(max_length=32, verbose_name='执行命令')),
                ('salt_callable', models.TextField(blank=True, null=True)),
                ('job', models.CharField(max_length=64)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('statues', models.PositiveSmallIntegerField(choices=[(0, '成功'), (1, '失败'), (2, '定时任务'), (3, '进行中'), ('NUll', '第一次配置')], default=2)),
                ('histroy', models.CharField(blank=True, max_length=16, null=True)),
                ('ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Hostname')),
            ],
            options={
                'verbose_name_plural': '操作命令',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=16, verbose_name='服务名称')),
                ('port', models.CharField(max_length=8)),
                ('files', models.CharField(max_length=32)),
                ('url', models.URLField(blank=True, null=True)),
                ('salt_leader', models.ManyToManyField(to='rest.Saltrun')),
            ],
            options={
                'verbose_name_plural': '服务',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_name', models.CharField(max_length=16, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '业务线',
            },
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, unique=True)),
                ('email', models.EmailField(blank=True, max_length=16, null=True)),
                ('onwatch', models.SmallIntegerField(choices=[(0, '值班'), (1, '休息'), (2, '协同')], default=2)),
            ],
            options={
                'verbose_name_plural': '运维人员',
            },
        ),
        migrations.AddField(
            model_name='hostname',
            name='role_type',
            field=models.ManyToManyField(blank=True, default=1, null=True, to='rest.Userprofile'),
        ),
        migrations.AddField(
            model_name='hostname',
            name='species_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.Species', verbose_name='业务线经理'),
        ),
        migrations.AlterUniqueTogether(
            name='saltrun',
            unique_together=set([('ip', 'job')]),
        ),
    ]