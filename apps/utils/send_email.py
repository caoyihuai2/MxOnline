# -*- coding:utf-8 -*-
from random import Random

from users.models import EmailVerifyRecord
from django.core.mail import send_mail

from MXOnline.settings import EMAIL_FROM
__author__ = 'cao.yh'
__date__ = '2018/3/20 上午9:18'


# 生成随机字符串
def generate_random_string(randomlength = 8):
    string = ''
    chars = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPKLJHGFDSAZXCVBNM1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(0, randomlength):
        string += chars[random.randint(0, length)]
    return string


# 发送邮箱注册信息
def send_register_mail(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = generate_random_string(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    # email_title = ""
    # email_body = ""

    if send_type == "register":
        email_title = "慕学网在线"
        email_body = "请点击下面链接激活账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

