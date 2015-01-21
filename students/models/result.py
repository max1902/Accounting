# -*- coding: utf-8 -*-
from django.db import models

class Result(models.Model):
    """Exam Model"""
    class Meta(object):
        verbose_name = u"Результат іспиту"
        verbose_name_plural = u"Результати іспитів"

    examname = models.ForeignKey('Exam',
        max_length=50,
        blank=False,
        verbose_name=u"Назва Предмету")

    stud = models.ForeignKey('Student',
        verbose_name=u"Студент")

    grade = models.IntegerField(
        default=u'4',
        verbose_name=u"Оцінка",
        )

#    def __unicode__(self):
#        if self.leader:
#            return u"%s %s" % (self.name_subject,self.name_teacher)
    def __unicode__(self):
        return "%s %s " % (self.stud.first_name, self.stud.last_name)
