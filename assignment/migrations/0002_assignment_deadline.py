# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 22, 51, 56, 764358)),
            preserve_default=False,
        ),
    ]
