# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    GENDER_ITEMS = (
        ("male", u"男"),
        ("female", u"女"),
    )

    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_ITEMS, default=u"female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y、%m", default="image/default")

    class Meta:
        verbose_name = verbose_name_plural = "用户信息"

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    TYPE_ITEMS = (
        ("register", "注册"),
        ("forget", "找回密码"),
    )

    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=TYPE_ITEMS, max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = verbose_name = "邮箱验证码"


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name_plural = verbose_name = "轮播图"