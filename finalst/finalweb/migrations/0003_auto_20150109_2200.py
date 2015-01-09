# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalweb', '0002_auto_20150109_1627'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Reference',
        ),
    ]
