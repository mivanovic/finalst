# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalweb', '0003_auto_20150207_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('reference', models.ForeignKey(to='finalweb.Reference')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
