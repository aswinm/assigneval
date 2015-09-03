# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assignment', '0002_assignment_deadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('sid', models.AutoField(serialize=False, primary_key=True)),
                ('answer', models.FileField(upload_to=b'answers')),
                ('submitted_at', models.DateTimeField()),
                ('assignment', models.ForeignKey(to='assignment.Assignment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
