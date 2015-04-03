# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exam import Exam
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.views.generic import UpdateView, CreateView, DeleteView
from ..models.students import Student
from ..models.groups import Group

from ..util import paginate, get_current_group


class ExamForm(ModelForm):
    class Meta:
        model = Exam

    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False

        # set form tag attributes
        if add_form:
            self.helper.form_action = reverse('exams_add')
        else:
            self.helper.form_action = reverse('exams_edit',
                kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        if add_form:
            submit = Submit('add_button', u'Додати',
                css_class="btn btn-primary")
        else:
            submit = Submit('save_button', u'Зберегти',
                css_class="btn btn-primary")

        self.helper.layout[-1] = FormActions(
            submit,
            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
        )

class ExamUpdateView(UpdateView):
    model = Exam
    template_name = 'students/create_update_exams.html'
    form_class = ExamForm
    success_msg = u'Екзамен успішно збережено!'
    error_msg = u'Редагування екзамена скасовано!'

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return u'%s?status_message=Екзамен успішно збережено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.success(self.request, self.error_msg)

            return HttpResponseRedirect(
                u'%s?status_message=Редагування екзамена відмінено' % reverse('home'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)



class ExamAddView(CreateView):
    model = Exam
    template_name = 'students/create_update_exams.html'
    form_class = ExamForm
    error_msg = u'Додавання екзамену скасовано'

    def get_success_url(self):
        #import pdb; pdb.set_trace()
        name_subject = unicode.encode(self.request.POST.get(u'name_subject', ''), 'utf8')
        success_message = 'Екзамен %s  успішно додано!' % (name_subject)
        messages.success(self.request, success_message)
        return u'%s?status_message=Екзамен %s успішно додано' % (reverse('home'),
            self.request.POST.get('name_subject', False))

    def post(self, request, *args, **kwargs):
        #import pdb; pdb.set_trace()
        if request.POST.get('cancel_button'):
            messages.success(self.request, self.error_msg)

            return HttpResponseRedirect(
                    u'%s?status_message=Додавання екзамену скасовано'
                                % reverse('home'))
        else:
            return super(ExamAddView, self).post(request, *args, **kwargs)


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'students/exams_confirm_delete.html'
    success_msg = u'Екзамен успішно видалено!'

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return u'%s?status_message=Екзамен успішно видалено!' % reverse('home')


def exams_list(request):

    current_group = get_current_group(request)
    if current_group:
        exams = Exam.objects.filter(name_group=current_group)
    else:
        exams = Exam.objects.all()
    
    exams = exams.order_by('time_exam')
    if request.GET.get('order_by', '') == '':
        request.GET.order_by = 'time_exam'
    order_by = request.GET.get('order_by', '')
    if order_by in ('name_subject', 'teacher', 'time_exam', 'name_group'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    context = paginate(exams,3,request,{}, var_name='exams')
    return render(request, 'students/exams_list.html', context)

