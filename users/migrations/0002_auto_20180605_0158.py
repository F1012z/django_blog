# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 01:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证码'},
        ),
    ]
