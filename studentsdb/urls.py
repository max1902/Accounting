from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.views.contact_admin import ContactView
from students.views.students import StudentUpdateView, StudentAddView, StudentDeleteView
from students.views.groups import GroupUpdateView, GroupAddView, GroupDeleteView
from students.views.exams import ExamUpdateView, ExamAddView, ExamDeleteView

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', StudentAddView.as_view(),
           name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(),
           name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', 'students.views.students.student_del',
           name='students_delete'),
    # url(r'^blog/', include('blog.urls')),
    
    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),    
    url(r'^groups/add/$', GroupAddView.as_view(),
           name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(),
           name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(),
           name='groups_delete'),

    # Visits urls
    url(r'^visits/$', 'students.views.visits.visits_list', name='visits'),
    url(r'^visits/add/$', 'students.views.groups.groups_add',
           name='visits_add'),
    url(r'^visits/(?P<mid>\d+)/edit/$', 'students.views.visits.visits_edit',
           name='visits_edit'),
    
    #exams
    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
    url(r'^exams/add/$', ExamAddView.as_view(),
           name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamUpdateView.as_view(),
           name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view(),
           name='exams_delete'),
    #result exam
    url(r'^result_exam/$', 'students.views.result_exam.result_list', name='result_list'),

    url(r'^admin/', include(admin.site.urls)),

    # Contact Admin Form
    url(r'^contact_admin/$', ContactView.as_view(), name='contact_admin'),


)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': MEDIA_ROOT}))
