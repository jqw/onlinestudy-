#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    # 列表显示
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    # 查找功能
    search_fields = ['name', 'mobile', 'course_name']
    # 筛选功能
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    # 列表显示
    list_display = ['studyuser', 'course', 'comments', 'add_time']
    # 查找功能
    search_fields = ['studyuser', 'course', 'comments']
    # 筛选功能
    list_filter = ['studyuser', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    # 列表显示
    list_display = ['studyuser', 'course', 'fav_id', 'fav_type']
    # 查找功能
    search_fields = ['studyuser', 'course', 'fav_id', 'fav_type']
    # 筛选功能
    list_filter = ['studyuser', 'course', 'fav_id', 'fav_type']


class UserMessageAdmin(object):
    # 列表显示
    list_display = ['studyuser', 'message', 'has_read', 'add_time']
    # 查找功能
    search_fields = ['studyuser', 'message', 'has_read']
    # 筛选功能
    list_filter = ['studyuser', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    # 列表显示
    list_display = ['studyuser', 'course', 'add_time']
    # 查找功能
    search_fields = ['studyuser', 'course']
    # 筛选功能
    list_filter = ['studyuser', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
