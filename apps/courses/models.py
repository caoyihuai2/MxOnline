# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from organization.models import CourseOrg

# Create your models here.


class Course(models.Model):
    DEGREE_ITEMS = (
        ("primary", "初级"),
        ("middle", "中级"),
        ("high", "高级"),
    )

    course_org = models.ForeignKey(CourseOrg, verbose_name="课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=DEGREE_ITEMS, max_length=10, verbose_name="难度")
    learn_time_minute = models.IntegerField(default=0, verbose_name="学习时长")
    learn_students_nums = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    category = models.CharField(max_length=20, default="后台开发", verbose_name="课程分类")
    tag = models.CharField(max_length=20, default="django", verbose_name="课程标签")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="封面")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "课程"

    def __unicode__(self):
        return self.name

    def get_lesson_nums(self):
        return self.lesson_set.count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]



class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "章节"


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "视频"


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="资源名称")
    download = models.FileField(max_length=100, verbose_name="资源路径", upload_to="course/resource/%Y/%m")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "课程资源"
