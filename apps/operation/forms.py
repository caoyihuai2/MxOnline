# -*- coding:utf-8 -*-
import re

__author__ = 'cao.yh'
__date__ = '2018/3/25 下午1:34'

from django import forms
from .models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_name(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p =re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            # 自定义错误信息
            raise forms.ValidationError("手机号码非法", code="mobile_invalid")