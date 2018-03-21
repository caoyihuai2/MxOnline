# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.views.generic.base import View

from users.form import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from users.models import UserProfile, EmailVerifyRecord
from utils.send_email import send_register_email


# 配置自定义的登录认证
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户登录模块
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=user_name, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html", {"username": user.username})
                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


# 用户注册模块
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"msg": "用户名已经存在", })
            else:
                password = request.POST.get("password", "")
                user_profile = UserProfile()
                user_profile.is_active = False
                user_profile.username = user_name
                user_profile.email = user_name
                user_profile.password = make_password(password)
                user_profile.save()

                send_register_email(user_profile.email, 'register')
                return render(request, "login.html")
        else:
            return render(request, "register.html", {'register_form': register_form})


# 用户激活
class UserActiveView(View):
    def get(self, request, active_code):
        # 从URL中提取active_code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_failed.html")
        return render(request, "login.html")


# 忘记密码
class ForgetPwdView(View):
    def get(self, request):
        forgetpwd_form = ForgetPwdForm()
        return render(request, "forgetpwd.html", {'forgetpwd_form': forgetpwd_form})

    def post(self, request):
        forgetpwd_form = ForgetPwdForm(request.POST)
        if forgetpwd_form.is_valid():
            email = request.POST.get("email", "")
            send_register_email(email, "forget")
            return render(request, "send_success.html")
        else:
            return render(request, "forgetpwd.html", {'forgetpwd_form': forgetpwd_form})


# 处理邮件链接
class ResetPwdView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {'email': email})
        else:
            return render(request, "active_failed.html", {})


# 修改密码
class ModifyPwdView(View):
    def post(self, request):
        modifypwd_form = ModifyPwdForm(request.POST)
        if modifypwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {'email': email, 'msg': "密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, "login.html")

        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {'email': email, 'modifypwd_form': modifypwd_form})
