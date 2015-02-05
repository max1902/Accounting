# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
from django.views.generic import UpdateView, CreateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.groups import Group
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions



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
    def clean_student_group(self):
        """Check if student is leader in any group.
        If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
#        students = Student.objects.all()
#        if students.first_name in self.cleaned_data['title']:
#            raise ValidationError(u'Студент все ще є у групі.', code='invalid')
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи.',
                    code='invalid')
        return self.cleaned_data['student_group']




#Views for Groups
#class GroupUpdateForm(ModelForm):
#    class Meta:
#        model = Group
#    def __init__(self, *args, **kwargs):
#        super(GroupUpdateForm, self).__init__(*args, **kwargs)
#
#        self.helper = FormHelper(self)
#
#        # set form tag attributes
#        self.helper.form_action = reverse('groups_edit',
#            kwargs={'pk': kwargs['instance'].id})
#        self.helper.form_method = 'POST'
#        self.helper.form_class = 'form-horizontal'
#
#        # set form field properties
#        self.helper.help_text_inline = True
#        self.helper.html5_required = True
#        self.helper.label_class = 'col-sm-2 control-label'
#        self.helper.field_class = 'col-sm-10'
#
#        # add buttons
#        self.helper.layout[-1] = FormActions(
#            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
#            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
#                                            )
#
#
#

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






#class GroupAddForm(ModelForm):
#    class Meta:
#        model = Group
#    def __init__(self, *args, **kwargs):
#        super(GroupAddForm, self).__init__(*args, **kwargs)
#
#        self.helper = FormHelper(self)
#
#        # set form tag attributes
#        self.helper.form_action = reverse('groups_add')
#        self.helper.form_method = 'POST'
#        self.helper.form_class = 'form-horizontal'
#
#        # set form field properties
#        self.helper.help_text_inline = True
#        self.helper.html5_required = True
#        self.helper.label_class = 'col-sm-2 control-label'
#        self.helper.field_class = 'col-sm-10'
#
#        # add buttons
#        self.helper.layout[-1] = FormActions(
#            Submit('add_button', u'Додати', css_class="btn btn-primary"),
#            Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
#                                            )
#    def clean_student_group(self):
#        """Check if student is leader in any group.
#        If yes, then ensure it's the same as selected group."""
#        # get group where current student is a leader
##        students = Student.objects.all()
##        if students.first_name in self.cleaned_data['title']:
##            raise ValidationError(u'Студент все ще є у групі.', code='invalid')
#        groups = Group.objects.filter(leader=self.instance)
#        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
#            raise ValidationError(u'Студент є старостою іншої групи.',
#                    code='invalid')
#        return self.cleaned_data['student_group']
#

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
    groups = Group.objects.all()
    #order_by sort
    if request.path =='/groups/':
        groups = groups.order_by('leader')
    order_by = request.GET.get('order_by','')
    if order_by in ('title','leader','id'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse',''):
            groups = groups.reverse()
    #paginator group
    paginator = Paginator(groups,3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999),
        #deliver last page of results
        groups = paginator.page(paginator.num_pages)
    return render(request, 'students/groups_list.html', {'groups':groups})

def groups_add(request):
    
    return HttpResponse('<h1>Group Add Form</h1>')





