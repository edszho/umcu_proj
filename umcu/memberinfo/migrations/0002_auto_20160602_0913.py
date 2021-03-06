# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('memberinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='None', max_length=40),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=2, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_primary',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='license_state',
            field=localflavor.us.models.USStateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='membership',
            field=models.CharField(choices=[('1', 'UM Student'), ('2', 'UM Grad Student'), ('3', 'UM Hospital'), ('4', 'UM Faculty/Staff'), ('5', 'Alumni'), ('6', 'Retiree'), ('7', 'WCC'), ('8', 'Family Member'), ('9', 'Current Member'), ('10', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='ssn',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
