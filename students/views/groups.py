# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse


#Views for Groups

def groups_list(request):
    groups = (
        {'id': 1,
         'name_group': u'МтЧ-21',
         'leader_group':u'Проказа Максим',  
         },
        {'id': 2,
         'name_group': u'МтМ-21',
         'leader_group':u'Вітя Подоба',  
         },
        {'id': 3,
         'name_group': u'МтК-44',
         'leader_group':u'Яроменко Ольга',  
         },
    )
    return render(request, 'students/groups_list.html', {'groups':groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


