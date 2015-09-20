# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(choices=[('', 'Unselected'), ('entered', 'Entered an Area'), ('exited', 'Exited an Area'), ('Do Button', 'Test Entry')], max_length=16),
        ),
    ]
