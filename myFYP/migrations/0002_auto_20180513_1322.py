# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-13 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFYP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='airCondition',
            new_name='Air_condition',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='buildingAge',
            new_name='Building_age',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='contactEmail',
            new_name='Conact_Name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='contactName',
            new_name='Contact_Email',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='contactPhone',
            new_name='Contact_Phone',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='freeParking',
            new_name='Free_parking',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='postalCode',
            new_name='Postal_code',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='propertyTitle',
            new_name='Property_Title',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='sqft_Measurement',
            new_name='Sqft_Measurement',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='swimmingPool',
            new_name='Swimming_pool',
        ),
    ]
