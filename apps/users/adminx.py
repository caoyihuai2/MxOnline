# -*- coding:utf-8 -*-
from xadmin import views

__author__ = 'cao.yh'
__date__ = '2018/3/18 上午10:41'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner, UserProfile


class BaseSetting(object):
    enable_themes = True  # 使用主题功能
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "MuXue Online"
    site_footer = "www.muxueonline.com"  # 设置xadmin 的title和footer
    menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ['nick_name', 'gender', 'address']
    search_fields = ['nick_name', 'gender', 'address']
    list_filter = ['nick_name', 'gender', 'address']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email']
    list_filter = ['code', 'email', 'send_type']


class BannerAdmin(object):
    list_display = ['title', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index', 'add_time']
    list_filter = ['title', 'url', 'index', 'add_time']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
#xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
