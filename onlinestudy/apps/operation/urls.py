#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
from django.conf.urls import include, url
from . import views

urlpatterns = [
   url('^userask/$', views.UserAskView.as_view(), name='userask'),
]
    
