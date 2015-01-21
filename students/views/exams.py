# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exam import Exam




def exams_list(request):
    exams = Exam.objects.all()
    exams = exams.order_by('time_exam')
    if request.GET.get('order_by', '') == '':
        request.GET.order_by = 'time_exam'
    order_by = request.GET.get('order_by', '')
    if order_by in ('name_subject', 'teacher', 'time_exam', 'name_group'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)
    return render(request, 'students/exams_list.html', {'exams': exams})

def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, vid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % vid)

def exams_delete(request, vid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % vid)