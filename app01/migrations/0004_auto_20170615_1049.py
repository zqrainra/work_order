# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20170615_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='m_time',
            field=models.DateField(),
        ),
    ]
