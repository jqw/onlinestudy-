from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 继承django中原有的user


class UserInfo(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default=u'')
    birthday = models.DateField(verbose_name=u'生日', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default=u'')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 图片上传需要pillow这个库
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # print
    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    # 可以区别是邮箱验证还是找回密码
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码')), max_length=20)
    # 这个now的时间一定要去掉括号不然会很据类生成的时间
    # 便于设置过期时间
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):

        return '{0}({1})'.format(self.code,self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y%m', verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

