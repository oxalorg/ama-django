# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ama', '0004_auto_20170428_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ama.Post'),
        ),
    ]
