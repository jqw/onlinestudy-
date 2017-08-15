#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from django.conf.urls import include, url
from django.contrib import admin
from .views import OrgListView, TeacherListView, OrgDetailView, \
    OrgCourseView, OrgDescView, OrgTeachersView

urlpatterns = [
    url(r'^orglist/$', OrgListView.as_view(), name='list'),
    url(r'^teacherlist/$', TeacherListView.as_view(), name='teacherlist'),
    url(r'^orgdetailhome/(\d*)/$', OrgDetailView.as_view(), name='orgdetail'),
    url(r'^orgdetailcourse/(\d*)$', OrgCourseView.as_view(), name='orgcourse'),
    url(r'^orgdesc/(\d*)$', OrgDescView.as_view(), name='orgdesc'),
    url(r'^orgteachers/(\d*)$', OrgTeachersView.as_view(), name='orgteachers'),
]
