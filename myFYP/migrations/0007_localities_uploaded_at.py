# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myFYP', '0006_auto_20180513_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='localities',
            name='uploaded_At',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
