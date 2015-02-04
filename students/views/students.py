# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime
from PIL import Image
from django.contrib import messages

from django.views.generic import UpdateView, CreateView, DeleteView
from ..models.students import Student
from ..models.groups import Group

from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


# Views for Students

class StudentForm(ModelForm):
    class Meta:
        model = Student

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False

        # set form tag attributes
        if add_form:
            self.helper.form_action = reverse('students_add')
        else:
            self.helper.form_action = reverse('students_edit',
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
##############################UPDATE STUDENT####################################
#class StudentUpdateForm(ModelForm):
#    class Meta:
#        model = Student
#    def __init__(self, *args, **kwargs):
#        super(StudentUpdateForm, self).__init__(*args, **kwargs)
#
#        self.helper = FormHelper(self)
#
#        # set form tag attributes
#        self.helper.form_action = reverse('students_edit',
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

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/create_update_students.html'
    form_class = StudentForm
    success_msg = u'Студента успішно збережено!'
    error_msg = u'Редагування студента скасовано!'

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return u'%s?status_message=Студента успішно збережено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.success(self.request, self.error_msg)

            return HttpResponseRedirect(
                u'%s?status_message=Редагування студента відмінено' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


##############################CREATE STUDENT####################################
#class StudentAddForm(ModelForm):
#    class Meta:
#        model = Student
#    def __init__(self, *args, **kwargs):
#        super(StudentAddForm, self).__init__(*args, **kwargs)
#
#        self.helper = FormHelper(self)
#
#        # set form tag attributes
#        self.helper.form_action = reverse('students_add')
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


class StudentAddView(CreateView):
    model = Student
    template_name = 'students/create_update_students.html'
    form_class = StudentForm
    error_msg = u'Додавання студента скасовано'

    def get_success_url(self):
        first_name = unicode.encode(self.request.POST.get(u'first_name', ''), 'utf8')
        last_name = unicode.encode(self.request.POST.get(u'last_name', ''), 'utf8')
        success_message = 'Студент %s %s успішно доданий!' % (
        first_name, last_name)
        messages.success(self.request, success_message)
        return u'%s?status_message=Студент %s %s успішно доданий' % (reverse('home'),
            self.request.POST.get('first_name', False),
            self.request.POST.get('last_name', False))

    def post(self, request, *args, **kwargs):
        
        if request.POST.get('cancel_button'):
            messages.success(self.request, self.error_msg)
            
            return HttpResponseRedirect(
                    u'%s?status_message=Додавання студента скасовано'
                                % reverse('home'))
        else:
            return super(StudentAddView, self).post(request, *args, **kwargs)



##############################DELETE STUDENT####################################
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    success_msg = u'Студента успішно видалено!'

    def get_success_url(self):
        messages.success(self.request, self.success_msg)
        return u'%s?status_message=Студента успішно видалено!' % reverse('home')







def students_list(request):

    students = Student.objects.all()
    #import pdb; pdb.set_trace()
    # order_by sort
    if request.path == '/':
       students = students.order_by('last_name')
    order_by = request.GET.get('order_by','')
    if order_by in ('last_name','first_name','ticket','id'):
        students = students.order_by(order_by)
        if request.GET.get('reverse',''):
            students = students.reverse()

    # paginate students
    paginator = Paginator(students,3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g. 9999),
        #deliver last page of results
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students':students})


def students_edit(request, pk):
    pk = int(pk)
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            data = { 'middle_name':request.POST.get('middle_name',''),
                     'notes':request.POST.get('notes','') }

            errors = {}
            first_name = request.POST.get('first_name').strip()
            if not first_name :
                errors['first_name'] = u'Правильно відредагуйте поле'
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u'Правильно відредагуйте поле'
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                errors['birthday'] = u"Правильно відредагуйте поле"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket','').strip()
            if not ticket:
                errors['ticket'] = u"Правильно відредагуйте поле"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group','').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]
                

            photo = request.FILES.get('photo','')
            if photo:
                try:
                    #import pdb; pdb.set_trace()
                    img = Image.open(photo)
                    file_size = request.FILES['photo'].size

                    if img.format in ('JPEG', 'PNG', 'BMP', 'GIF'):
                        if file_size < 2 * 1024 * 1024:
                            data['photo'] = photo
                        else:
                            errors['photo'] = u'Розмір файлу зображення неможе\
                                      перевищувати 2Мб'
                    else:
                        errors['photo'] = u'Невірний формат зображення напр.\
                                      (*.bmp, *.png або *.jpeg)'
                except Exception:
                    errors['photo'] = u'Невірний формат зображення напр.\
                                      (*.bmp, *.png або *.jpeg)'

            if not errors:
                student = Student(**data)
                student.save()
                return HttpResponseRedirect(
            u'%s?status_message=Студента %s %s успішно відредаговано! ' % (
                        reverse('home'), student.first_name, student.last_name))
            else:
                #render form with errors and previous  user input
                return render(request, 'students/students_add.html',
                              {'groups':Group.objects.all().order_by('title'),
                              'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
        u'%s?status_message=Редагування студента скасовано!' % reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
            {'groups': Group.objects.all().order_by('title')})

def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # TODO: validate input from user
            errors={}

            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            #validate user input
            first_name = request.POST.get('first_name','').strip()
            if not first_name:
                #messages.add_message(request, FIRST_NAME, u"Ім'я є обов'язковим")
                errors['first_name'] = u"Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name','').strip()
            if not last_name:
                #messages.add_message(request, LAST_NAME, u"Прізвище є обов'язковим")
                errors['last_name'] = u"Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday','').strip()
            if not birthday:
                #messages.add_message(request, BIRTHDAY, u"Дата народження є обов'язковою")
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    #messages.add_message(request, BIRTHDAY,
                     #      u"Введіть коректний формат дати (напр. 1984-12-30)")
                    errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket','').strip()
            if not ticket:
                #messages.add_message(request, TICKET, u"Номер білета є обов'язковим")
                errors['ticket'] = u"Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group','').strip()
            if not student_group:
                #messages.add_message(request, STUDENT_GROUP, u"Оберіть групу для студента")
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    #messages.error(request, u"Оберіть коректну групу")
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo','')
            if photo:
                try:
                    #import pdb; pdb.set_trace()
                    img = Image.open(photo)
                    file_size = request.FILES['photo'].size

                    if img.format in ('JPEG', 'PNG', 'BMP', 'GIF'):
                        if file_size < 2 * 1024 * 1024:
                            data['photo'] = photo
                        else:
                     #       messages.add_message(request, PHOTO,
                    #u'Розмір файлу зображення неможе перевищувати 2Мб')
                            errors['photo'] = u'Розмір файлу зображення неможе\
                                      перевищувати 2Мб'
                    else:
                      #  messages.add_message(request, PHOTO,
                    #u'Невірний формат зображення напр.\
                                      #(*.bmp, *.png або *.jpeg)')
                        errors['photo'] = u'Невірний формат зображення напр.\
                                      (*.bmp, *.png або *.jpeg)'
                except Exception:
                    #messages.add_message(request, PHOTO,
                    #u'Невірний формат зображення напр.\
                     #                 (*.bmp, *.png або *.jpeg)')
                    errors['photo'] = u'Невірний формат зображення напр.\
                                      (*.bmp, *.png або *.jpeg)'

            #save students
            if not errors:
                student = Student(**data)
                student.save()
                #messages.info(request, 'Yo! There are new comments on your photo!')
                #redirect to students list
                return HttpResponseRedirect(
            u'%s?status_message=Студента %s %s успішно додано! ' % (reverse('home'), student.first_name, student.last_name))
            else:
                #render form with errors and previous  user input
                return render(request, 'students/students_add.html',
                              {'groups':Group.objects.all().order_by('title'),
                              'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
        u'%s?status_message=Додавання студента скасовано!' % reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html', {'groups': Group.objects.all().order_by('title')})
