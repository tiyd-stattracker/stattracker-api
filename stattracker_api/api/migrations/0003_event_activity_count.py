# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151027_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='activity_count',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
