# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20160518_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
