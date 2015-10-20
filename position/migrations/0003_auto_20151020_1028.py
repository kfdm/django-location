# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0002_auto_20150920_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(choices=[('', 'Unselected'), ('entered', 'Entered an Area'), ('exited', 'Exited an Area'), ('Do Button', 'Test Entry'), ('Do Note', 'Manual Entry')], max_length=16),
        ),
    ]
