# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exam import Exam
from ..models.result import Result




def result_list(request):
    results = Result.objects.all()
    return render(request, 'students/result_list.html', {'results': results})