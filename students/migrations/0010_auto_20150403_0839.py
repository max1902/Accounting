# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20150402_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='name_group',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0433\u0440\u0443\u043f\u0438', blank=True, to='students.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exam',
            name='teacher',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447'),
            preserve_default=True,
        ),
    ]
