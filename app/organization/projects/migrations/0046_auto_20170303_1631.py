# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0045_auto_20170303_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsimpleimage',
            name='file',
            field=models.FileField(max_length=1024, upload_to='images', verbose_name='Image'),
        ),
    ]
