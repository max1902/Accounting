# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20150121_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.IntegerField(default=4, null=True, verbose_name='\u041e\u0446\u0456\u043d\u043a\u0430')),
                ('examname', models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0443', to='students.Exam', max_length=50)),
                ('stud', models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student')),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
            bases=(models.Model,),
        ),
    ]
