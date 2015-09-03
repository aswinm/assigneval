# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_plagiarism',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
