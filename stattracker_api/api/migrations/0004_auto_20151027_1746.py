# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_event_activity_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('activity_date', models.DateField()),
                ('activity_count', models.PositiveSmallIntegerField()),
                ('activity', models.ForeignKey(to='api.Activity', related_name='logs')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='activity',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
