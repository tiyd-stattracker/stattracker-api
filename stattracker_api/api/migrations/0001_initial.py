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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('activity_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('activity_date', models.DateField()),
                ('activity_count', models.PositiveSmallIntegerField()),
                ('activity', models.ForeignKey(related_name='logs', to='api.Activity')),
            ],
        ),
    ]
