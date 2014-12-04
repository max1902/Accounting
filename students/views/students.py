# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse


# Views for Students


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Андрій',
         'last_name': u'Корост',
         'ticket': 2123,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': u'Максим',
         'last_name': u'Проказа',
         'ticket': 2000,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': u'Ольга',
         'last_name': u'Яроменко',
         'ticket': 2050,
         'image': 'img/3.jpg'},
    )
    return render(request, 'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

