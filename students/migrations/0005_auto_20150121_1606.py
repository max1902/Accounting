# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='time_exam',
            field=models.DateTimeField(null=True, verbose_name='\u0427\u0430\u0441 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443'),
            preserve_default=True,
        ),
    ]
