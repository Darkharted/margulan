from django.urls import path
from . import views

urlpatterns = [
    path('subjects/$', views.SubjectListView.as_view(), name='subject_list'),
    path('subjects/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='subject_detail'),
    path(r'^courses/(?P<pk>\d+)/enroll/$', views.CourseEnrollView.as_view(), name='course_enroll'),

]
