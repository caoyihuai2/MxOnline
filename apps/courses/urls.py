# -*- coding:utf-8 -*-
__author__ = 'cao.yh'
__date__ = '2018/3/26 下午5:42'
from django.conf.urls import url, include
from .views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="course_list")
]