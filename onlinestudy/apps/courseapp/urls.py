#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
from django.conf.urls import include, url
from django.contrib import admin
from .views import CourseListView

urlpatterns = [
   url('^courselist/$', CourseListView.as_view(), name='list'),
]


    
