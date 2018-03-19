# -*- coding:utf-8 -*-
__author__ = 'cao.yh'
__date__ = '2018/3/19 上午10:25'
from django import forms


class LoginForm(forms.Form):
    # username和password必须同HTML的form中name字段相同的值
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
