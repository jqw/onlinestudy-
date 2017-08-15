#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    # 列表显示
    list_display = ['name', 'desc', 'add_time']
    # 查找功能
    search_fields = ['name', 'desc']
    # 筛选功能
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    # 列表显示
    list_display = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image',
                    'address', 'city']
    # 查找功能
    search_fields = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image',
                     'address', 'city']
    # 筛选功能
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image',
                   'address', 'city']


class TeacherAdmin(object):
    # 列表显示
    list_display = ['org', 'name', 'work_years',
                    'work_company', 'work_position', 'points',
                    'click_nums', 'fav_nums', 'add_time']
    # 查找功能
    search_fields = ['org', 'name', 'work_years',
                     'work_company', 'work_position', 'points',
                     'click_nums', 'fav_nums']
    # 筛选功能
    list_filter = ['org', 'name', 'work_years',
                   'work_company', 'work_position', 'points',
                   'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
