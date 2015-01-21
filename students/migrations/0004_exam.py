# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_subject', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('teacher', models.CharField(max_length=50, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447', blank=True)),
                ('time_exam', models.DateField(null=True, verbose_name='\u0427\u0430\u0441 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443')),
                ('name_group', models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0433\u0440\u0443\u043f\u0438', to='students.Group', null=True)),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
            bases=(models.Model,),
        ),
    ]
