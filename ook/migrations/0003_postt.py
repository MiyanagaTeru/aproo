# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ook', '0002_past'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('select', models.BooleanField()),
            ],
        ),
    ]