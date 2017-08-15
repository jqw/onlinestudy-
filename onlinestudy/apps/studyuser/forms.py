#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
# 表单验证
from django import forms
from captcha.fields import CaptchaField


# 登录的条件验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=12)


# 根据前面网页输入的字段分别进行约束
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=12)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


# 忘记密码，提交账号和验证码
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


# 验证重置密码
class ResetPwdForm(forms.Form):
    password = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)