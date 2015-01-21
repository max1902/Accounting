from django.contrib import admin
from .models.groups import Group
from .models.students import Student
from .models.exam import Exam
# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
