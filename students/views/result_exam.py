# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exam import Exam
from ..models.result import Result
from ..models.students import Student

from ..util import paginate




def result_list(request):
    results = Result.objects.all()

    context = paginate(results, 5, request, {}, var_name='results')
    return render(request, 'students/result_list.html', context)