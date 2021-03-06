# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20170628_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrymap',
            name='name',
            field=models.CharField(default='kenya', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='countrymap',
            name='country_represented',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='maps.Country'),
        ),
    ]
