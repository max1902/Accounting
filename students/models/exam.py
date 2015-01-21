# -*- coding: utf-8 -*-
from django.db import models

class Exam(models.Model):
    """Exam Model"""
    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"

    name_subject = models.CharField(
        max_length=50,
        blank=False,
        verbose_name=u"Назва Предмету")

    teacher = models.CharField(
        max_length=50,
        verbose_name=u"Викладач",
        blank=True,
        null=True)

    time_exam = models.DateTimeField(
        blank=False,
        verbose_name=u"Час екзамену",
        null=True)
   
    name_group = models.ForeignKey('Group',
        verbose_name=u"Назва групи",
        blank=False,
        null=True)

#    def __unicode__(self):
#        if self.leader:
#            return u"%s %s" % (self.name_subject,self.name_teacher)
    def __unicode__(self):
        return "%s %.16s" % (self.name_subject, self.time_exam,)
