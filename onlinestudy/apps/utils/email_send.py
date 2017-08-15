#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
__author__ = 'jqw'
__date__ = '2017/7/6'
from random import Random
from studyuser.models import EmailVerifyRecord
# 发送邮箱
from django.core.mail import send_mail
from onlinestudy.settings import EMAIL_FROM


# 发送邮件,短信验证码
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDddEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength - 1):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, sent_type='register'):
    email_record = EmailVerifyRecord()
    # 随机生成字符,并将发送的内容保存在数据库中
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = sent_type
    email_record.save()

    email_title = ''
    email_body = ''
    if sent_type == 'register':
        email_title = '幕学在线网注册激活'
        email_body = '激活链接：http://127.0.0.1:8899/studyuser/active/{0}'.format(code)
        # django提供了内部函数来实现发送邮件
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return 'ok'

    elif sent_type == 'forget':
        email_title = '幕学在线网密码重置'
        email_body = '激活链接：http://127.0.0.1:8899/studyuser/activepwd/{0}'.format(code)
        # django提供了内部函数来实现发送邮件
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return 'ok'
