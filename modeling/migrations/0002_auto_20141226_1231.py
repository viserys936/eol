# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='id',
        ),
        migrations.AlterField(
            model_name='creature',
            name='c_id',
            field=models.TextField(primary_key=True, serialize=False, default=''),
        ),
    ]
