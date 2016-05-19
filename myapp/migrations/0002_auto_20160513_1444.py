# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='online',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'online',
            },
        ),
        migrations.AddField(
            model_name='mysite',
            name='online',
            field=models.ForeignKey(default=1, to='myapp.online'),
        ),
    ]
