# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(unique=True, max_length=50)),
                ('points', models.PositiveIntegerField(default=0)),
                ('points_counter', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True, editable=False)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
