# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='c_time',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='f_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='m_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='m_time',
            field=models.DateField(auto_now=True),
        ),
    ]
