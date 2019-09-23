# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-12 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(blank=True, max_length=64, null=True)),
                ('block_id', models.IntegerField(blank=True, null=True)),
                ('signature', models.IntegerField(blank=True, null=True)),
                ('x', models.DecimalField(decimal_places=14, max_digits=17)),
                ('y', models.DecimalField(decimal_places=14, max_digits=17)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('angle', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]