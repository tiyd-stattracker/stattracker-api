# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('activity_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='activity_date',
            new_name='start_date',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='activity_count',
        ),
        migrations.AddField(
            model_name='event',
            name='activity',
            field=models.ForeignKey(to='api.Activity', related_name='events'),
        ),
    ]
