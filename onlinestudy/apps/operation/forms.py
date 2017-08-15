#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import re

__author__ = 'jqw'
__date__ = '2017/7/6'
# 表单验证
from django import forms

from .models import UserAsk


class UserAskForm(forms.ModelForm):
    # 新扩展的字段
    # newArgs = forms.CharField(required=True, min_length=5)
    class Meta:
        # 只定从那个model生成
        model = UserAsk
        # 只定哪些是需要的字段字段
        fields = ['name', 'mobile', 'course_name']

    # 添加额外的验证方法
    def clean_mobile(self):
        '''
        验证手机号是否合法
        :return:
        '''
        # 获取表单传递过来的值
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')
