#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.mylogin, name='login'),
    # url(r'^handlelogin/$', views.handlelogin, name='handlelogin'),
    # 调用类的登录方法
    url(r'^handlelogin/$', views.LoginView.as_view(), name='handlelogin'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', views.ActiveUserView.as_view(), name='active'),
    url(r'^forgetpwd/$', views.ForgetView.as_view(), name='forget_pwd'),
    url(r'^activepwd/(?P<reset_code>.*)/$', views.ActivePwdView.as_view(), name='active_pwd'),
    url(r'^resetpwd/$', views.ResetPWDView.as_view(), name='resetpwd'),
    url(r'^test/$', views.test),
]
