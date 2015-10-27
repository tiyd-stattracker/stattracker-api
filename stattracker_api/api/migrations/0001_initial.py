# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('activity_name', models.CharField(max_length=255)),
                ('activity_date', models.DateField()),
                ('activity_count', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
