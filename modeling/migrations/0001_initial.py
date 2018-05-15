# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('c_id', models.TextField(default='')),
                ('s_name', models.TextField(default='')),
                ('c_name', models.TextField(default='')),
                ('category', models.TextField(default='')),
                ('iucn_level', models.TextField(default='')),
                ('level', models.TextField(default='')),
                ('location', models.TextField(default='')),
                ('location_number', models.TextField(default='')),
                ('location_style', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
