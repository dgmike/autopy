# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160824_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('model', models.CharField(db_index=True, max_length=100)),
                ('color', models.CharField(db_index=True, max_length=100)),
                ('rotated', models.PositiveIntegerField(blank=True, db_index=True)),
                ('motor', models.CharField(db_index=True, max_length=100)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Manufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]