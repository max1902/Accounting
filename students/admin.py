# -*- coding: utf-8 -*-
from django.contrib import admin
from .models.groups import Group
from .models.students import Student
from .models.exam import Exam
from .models.result import Result
from .models.monthjournal import MonthJournal
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
# Register your models here.




#xdsvfsd

class StudentFormAdmin(ModelForm):
    def clean_student_group(self):
        """Check if student is leader in any group.
            If yes, then ensure it's the same as selected group."""
        # get group where current student is a leader
        #import pdb; pdb.set_trace()
        groups = Group.objects.filter(leader=self.instance)
        
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи.',
                    code='invalid')
        return self.cleaned_data['student_group']



class GroupFormAdmin(ModelForm):

    def clean_leader(self):
        #import pdb; pdb.set_trace()
        st = Student.objects.filter(student_group=self.instance)
        if self.cleaned_data['leader'] not in list(st):
            raise ValidationError(u'Староста повинен бути у своїй групі.',
                    code='invalid')
            return self.cleaned_data['None']
        return self.cleaned_data['leader']
        

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        
        return reverse('students_edit', kwargs={'pk':obj.id})



class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title', 'leader']
    #list_editable = ['leader']
    ordering = ['title']
    list_filter = ['title']
    list_per_page = 5
    search_fields = ['title', 'leader']
    form = GroupFormAdmin

    def view_on_site(self, obj):

        return reverse('groups_edit', kwargs={'pk':obj.id})

class ExamAdmin(admin.ModelAdmin):
    list_display = ['name_subject', 'name_group', 'teacher']
    list_display_links = ['name_subject', 'teacher']
    list_editable = ['name_group']
    ordering = ['teacher']
    list_filter = ['teacher']
    list_per_page = 5
    search_fields = ['teacher', 'name_subject']

    def view_on_site(self, obj):

        return reverse('exams_edit', kwargs={'pk':obj.id})



admin.site.register(Student,StudentAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Result)
admin.site.register(MonthJournal)