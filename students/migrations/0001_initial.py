# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_subject', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0443')),
                ('teacher', models.CharField(max_length=50, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
                ('time_exam', models.DateTimeField(null=True, verbose_name='\u0427\u0430\u0441 \u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0443')),
                ('notes_exam', models.CharField(max_length=50, null=True, verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0406\u0441\u043f\u0438\u0442',
                'verbose_name_plural': '\u0406\u0441\u043f\u0438\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('present_day1', models.BooleanField(default=False)),
                ('present_day2', models.BooleanField(default=False)),
                ('present_day3', models.BooleanField(default=False)),
                ('present_day4', models.BooleanField(default=False)),
                ('present_day5', models.BooleanField(default=False)),
                ('present_day6', models.BooleanField(default=False)),
                ('present_day7', models.BooleanField(default=False)),
                ('present_day8', models.BooleanField(default=False)),
                ('present_day9', models.BooleanField(default=False)),
                ('present_day10', models.BooleanField(default=False)),
                ('present_day11', models.BooleanField(default=False)),
                ('present_day12', models.BooleanField(default=False)),
                ('present_day13', models.BooleanField(default=False)),
                ('present_day14', models.BooleanField(default=False)),
                ('present_day15', models.BooleanField(default=False)),
                ('present_day16', models.BooleanField(default=False)),
                ('present_day17', models.BooleanField(default=False)),
                ('present_day18', models.BooleanField(default=False)),
                ('present_day19', models.BooleanField(default=False)),
                ('present_day20', models.BooleanField(default=False)),
                ('present_day21', models.BooleanField(default=False)),
                ('present_day22', models.BooleanField(default=False)),
                ('present_day23', models.BooleanField(default=False)),
                ('present_day24', models.BooleanField(default=False)),
                ('present_day25', models.BooleanField(default=False)),
                ('present_day26', models.BooleanField(default=False)),
                ('present_day27', models.BooleanField(default=False)),
                ('present_day28', models.BooleanField(default=False)),
                ('present_day29', models.BooleanField(default=False)),
                ('present_day30', models.BooleanField(default=False)),
                ('present_day31', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '\u041c\u0456\u0441\u044f\u0447\u043d\u0438\u0439 \u0416\u0443\u0440\u043d\u0430\u043b',
                'verbose_name_plural': '\u041c\u0456\u0441\u044f\u0447\u043d\u0456 \u0416\u0443\u0440\u043d\u0430\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.IntegerField(default='4', verbose_name='\u041e\u0446\u0456\u043d\u043a\u0430')),
                ('examname', models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u041f\u0440\u0435\u0434\u043c\u0435\u0442\u0443', to='students.Exam', max_length=50)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u0456\u0441\u043f\u0438\u0442\u0443',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0438 \u0456\u0441\u043f\u0438\u0442\u0456\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041f\u043e-\u0431\u0430\u0442\u044c\u043a\u043e\u0432\u0456', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('ticket', models.CharField(max_length=256, verbose_name='\u0411\u0456\u043b\u0435\u0442')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
                ('student_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u0413\u0440\u0443\u043f\u0430', to='students.Group', null=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': 'C\u0442\u0443\u0434\u0435\u043d\u0442',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='result',
            name='stud',
            field=models.ForeignKey(verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(unique_for_month=b'date', verbose_name='\u0421\u0442\u0443\u0434\u0435\u043d\u0442', to='students.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='students.Student', verbose_name='\u0421\u0442\u0430\u0440\u043e\u0441\u0442\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exam',
            name='name_group',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u0437\u0432\u0430 \u0433\u0440\u0443\u043f\u0438', to='students.Group', null=True),
            preserve_default=True,
        ),
    ]
