# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalweb', '0004_refimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refimages',
            old_name='image',
            new_name='file',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='file',
        ),
    ]
