# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0004_submission_is_plagiarism'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='grade',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='score',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
