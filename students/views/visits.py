# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse


# Views for Visits


def visits_list(request):
    visits = (
        {'id': 1,
         'student_name': u'Проказа Максим',
         },
        {'id': 2,
         'student_name': u'Вітя Подоба',
         },
        {'id': 3,
         'student_name': u'Яроменко Ольга',
         },
    )
    return render(request, 'students/visits_list.html', {'visits':visits})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def visits_edit(request, mid):
    return HttpResponse('<h1>Edit Student %s</h1>' % mid)


