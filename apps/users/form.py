# -*- coding:utf-8 -*-
__author__ = 'cao.yh'
__date__ = '2018/3/19 上午10:25'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # username和password必须同HTML的form中name字段相同的值
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetPwdForm(forms.Form):
    email = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)