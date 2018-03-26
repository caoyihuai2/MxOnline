# -*- coding:utf-8 -*-
__author__ = 'cao.yh'
__date__ = '2018/3/25 下午1:39'

from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavOrgView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^org_home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^org_course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^org_desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    url(r'^add_fav/$', AddFavOrgView.as_view(), name="add_fav")
]