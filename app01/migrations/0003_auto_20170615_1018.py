# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170615_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='m_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='c_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='f_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='m_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
