# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.
from courses.models import Course
from users.models import UserProfile


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "用户咨询"


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户名")
    course = models.ForeignKey(Course, verbose_name="课程名")
    comments = models.CharField(max_length=200, verbose_name="评论详情")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "课程评论"


class UserFavorite(models.Model):
    TYPE_ITEMS = (
        (1, "课程"),
        (2, "课程机构"),
        (3, "讲师"),
    )

    user = models.ForeignKey(UserProfile, verbose_name="用户名")
    fav_id = models.IntegerField(default=0, verbose_name="数据id")
    fav_type = models.IntegerField(choices=TYPE_ITEMS, default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "用户收藏"


class UserMessage(models.Model):
    # user=0:全体user
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "用户消息"


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户名")
    course = models.ForeignKey(Course, verbose_name="课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "用户课程"