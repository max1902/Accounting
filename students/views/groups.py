# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
from django.views.generic import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.groups import Group
from ..models.students import Student
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.forms import ModelForm, ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..util import paginate, get_current_group

class GroupForm(ModelForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False

        # set form tag attributes
        if add_form:
            self.helper.form_action = reverse('groups_add')
        else:
            self.helper.form_action = reverse('groups_edit',
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

    def clean_leader(self):

        st = Student.objects.filter(student_group=self.instance)
        #groups = Group.objects.filter(leader=self.instance)
        #import pdb; pdb.set_trace()
#        if len(st) > 0 and self.cleaned_data['leader'] != groups[0]:
#            raise ValidationError(u'Студент.',
#                    code='invalid')
#        if self.cleaned_data['leader'] not in list(st):
#            raise ValidationError(u'Староста повинен бути у своїй групі.',
#                    code='invalid')
            
        return self.cleaned_data['leader']



class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'students/create_update_groups.html'
    form_class = GroupForm
    success_msg = u'Групу успішно збережено!'
    error_msg = u'Редагування групи скасовано!'

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return u'%s?status_message=Групу успішно збережено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.success(self.request, self.error_msg)

            return HttpResponseRedirect(
                u'%s?status_message=Редагування групи відмінено' % reverse('home'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupAddView(CreateView):
    model = Group
    template_name = 'students/create_update_groups.html'
    form_class = GroupForm
    error_msg = u'Додавання групи скасовано'

    def get_success_url(self):
        title = unicode.encode(self.request.POST.get(u'title', ''), 'utf8')
        success_message = 'Групу %s  успішно додано!' % (title)
        messages.success(self.request, success_message)
        return u'%s?status_message=Група %s успішно додана' % (reverse('home'),
            self.request.POST.get('title', False))

    def post(self, request, *args, **kwargs):
        
        if request.POST.get('cancel_button'):
            messages.success(self.request, self.error_msg)
            
            return HttpResponseRedirect(
                    u'%s?status_message=Додавання групи скасовано'
                                % reverse('home'))
        else:
            return super(GroupAddView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'
    success_msg = u'Групу успішно видалено!'

    def get_success_url(self):
        #messages.success(self.request, self.success_msg)
        return u'%s?status_message=Групу успішно видалено!' % reverse('home')


def groups_list(request):

    current_group = get_current_group(request)
    if current_group:
        groups = Group.objects.filter(id=current_group.id)
    else:
        groups = Group.objects.all()
    order_by = request.GET.get('order_by','')
    if order_by in ('title','leader','id'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse',''):
            groups = groups.reverse()
    #paginator group
    context = paginate(groups, 2,request, {}, var_name='groups')

    return render(request, 'students/groups_list.html', context)

def groups_add(request):
    
    return HttpResponse('<h1>Group Add Form</h1>')
