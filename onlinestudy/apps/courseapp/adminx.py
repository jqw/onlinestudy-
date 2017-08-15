#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
from .models import Course, Lesson, Video, CourseResource
import xadmin


class CourseAdmin(object):
    # 列表显示
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time', 'course_org', 'students', 'course_nums']
    # 查找功能
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                     'course_org', 'students', 'course_nums']
    # 筛选功能
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time', 'course_org', 'students', 'course_nums']


class LessonAdmin(object):
    # 列表显示
    list_display = ['course', 'name', 'add_time']
    # 查找功能
    search_fields = ['course', 'name']
    # 筛选功能，如果是外键course__name
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    # 查找功能,不能有时间
    search_fields = ['lesson', 'name']
    # 筛选功能，如果是外键course__name
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    # 查找功能,不能有时间
    search_fields = ['course', 'name', 'download']
    # 筛选功能，如果是外键course__name
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
