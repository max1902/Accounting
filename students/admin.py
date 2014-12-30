from django.contrib import admin
from .models.groups import Group
from .models.students import Student
# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
