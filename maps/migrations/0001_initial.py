# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('defaultmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='maps.DefaultModel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('maps.defaultmodel',),
        ),
        migrations.CreateModel(
            name='CountryMap',
            fields=[
                ('defaultmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='maps.DefaultModel')),
                ('border_type', models.CharField(choices=[('PR', 'Provincial'), ('CTY', 'County'), ('CNY', 'Constituency'), ('PLN', 'Plain')], default='PLN', max_length=3)),
            ],
            bases=('maps.defaultmodel',),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('defaultmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='maps.DefaultModel')),
                ('name', models.CharField(max_length=200)),
            ],
            bases=('maps.defaultmodel',),
        ),
    ]