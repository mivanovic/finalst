# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='file',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
