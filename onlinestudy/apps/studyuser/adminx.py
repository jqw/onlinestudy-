#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


# 全局设置使用主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# 针对所有的修改
class GlobalSettings(object):
    site_title = '幕学后台管理系统'
    site_footer = '幕学在线网'
    menu_style = 'accordion'


# 这里继承的是object
class EmailVerifyRecordAdmin(object):
    # 列表显示
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 查找功能
    search_fields = ['code', 'email', 'send_type']
    # 筛选功能
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 列表显示
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 查找功能
    search_fields = ['title', 'image', 'url', 'index']
    # 筛选功能
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
