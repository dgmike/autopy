# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='deleted_at',
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]