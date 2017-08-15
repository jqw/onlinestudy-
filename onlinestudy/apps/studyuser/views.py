# _*_ encoding:utf-8 _*_
from django.shortcuts import render
# django中处理用户登录的模块
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import UserInfo
# django中支持自定义用户名的验证方式
from django.contrib.auth.backends import ModelBackend
# 密码进行加密
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .models import UserInfo, EmailVerifyRecord
# 基于类的方式做认证
from django.views.generic.base import View
# 将from表单引入进来
from studyuser.forms import LoginForm, RegisterForm, ForgetPwdForm, ResetPwdForm
# 发送邮件的工具类
from utils.email_send import send_register_email


# 自定义登录的逻辑,登录的时候输入的是邮箱也可以作为用户名
# 1.自定义个一个类，继承ModelBackend
# 2.重写authenticate方法，定义验证的方式
# 3.配置到setting中AUTHENTICATION_BACKENDS = (
#    'studyuser.views.CustomBackend',
# )
class CustomBackend(ModelBackend):
    # 重写认证方法
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(Q(username=username) | Q(email=username))
            # 验证密码信息
            if user.check_password(password):
                return user
        except Exception as e:

            return None


# Create your views here.
def index(request):
    return render(request, 'index.html')


# 基于类的方式处理登录
# 继承view重写get,post方法
# 在url中配置 url(r'^handlelogin/$', views.LoginView.as_view(), name='handlelogin'),
class LoginView(View):
    # 是view自带的方法
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        # 先进行from表单
        # 在应用下创建from.py在里面定义类
        # class LoginForm(forms.Form):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # 调django自带的用户名和密码验证,需要指明用户名和密码
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # django自带的login方法,在定义函数的时候不要和系统默认的函数名一样
                # 在判断用户是否激活邮箱
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户没有激活'})
            else:
                return render(request, 'login.html', {'msg': '登录名或者密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


# login和handlelogin可以处理为一个方法，一个get和post方法进行区别
def mylogin(request):
    return render(request, 'login.html')


# 登录功能处理
# def handlelogin(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         # 调django自带的用户名和密码验证,需要指明用户名和密码
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             # django自带的login方法,在定义函数的时候不要和系统默认的函数名一样
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'msg': '登录名或者密码错误'})
#     elif request.method == 'GET':
#         return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html')


# 注册功能
class RegisterView(View):
    def get(self, request):
        # get请求注册功能
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            human = True
            # 验证邮箱是否注册过
            user_name = request.POST.get('email', '')
            if UserInfo.objects.filter(email=user_name):
                # 回传from是为了回填用户输入的数据
                return render(request, 'register.html', {'register_form': register_form, 'msg': '该用户已经存在'})

            pass_word = request.POST.get('password', '')
            user_info = UserInfo()
            user_info.username = user_name
            user_info.email = user_name
            # 默认状态这个是True
            user_info.is_active = False
            user_info.password = make_password(pass_word)
            user_info.save()
            # 发送邮件进行激活
            result = send_register_email(user_name, 'register')
            # 注册完成进入登录界面
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


# 激活邮箱
class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for recorde in all_records:
                email = recorde.email
                # 修改用户激活状态
                user = UserInfo.objects.get(email=email)
                user.is_active = True
                user.save()

            return render(request, 'login.html')
        else:
            # 验证失败
            return render(request, 'active_fail.html')


# 忘记密码
class ForgetView(View):
    def get(self, request):
        forget_form = ForgetPwdForm()
        context = {'forget_form': forget_form}
        return render(request, 'forgetpwd.html', context)

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            # 如果存在该账号进行找回
            if UserInfo.objects.filter(email=email).count() > 0:
                # 如果验证码和用户名正确
                # 发送邮件进行找回email, sent_type='register'
                send_register_email(email, sent_type='forget')
                # 邮件发送成功
                return render(request, 'send_success.html')
            else:
                context = {'forget_form': forget_form}
                return render(request, 'forgetpwd.html', context)
        else:
            # 验证错误
            context = {'forget_form': forget_form}
            return render(request, 'forgetpwd.html', context)


# 验证密码激活
class ActivePwdView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        email = all_records[0].email
        if all_records:
            # 需要保存一个需要修改的值
            return render(request, 'password_reset.html', {'email': email})
        else:
            # 验证失败
            return render(request, 'active_fail.html')


# 重置密码
class ResetPWDView(View):
    def post(self, request):
        resetform = ResetPwdForm(request.POST)
        email = request.POST.get('email', '')
        if resetform.is_valid():
            # 如果验证通过
            # 查找相互修改的对象
            userinfo = UserInfo.objects.filter(email=email)[0]
            password = request.POST.get('password', '')
            password2 = request.POST.get('password2', '')
            if password == password2:
                userinfo.password = make_password(password)
                userinfo.save()
                # 修改密码成功
                return render(request, 'login.html')
            else:
                # 两次输入密码不一致
                return render(request, 'password_reset.html', {'email': email})
        else:
            # 如果验证失败
            return render(request, 'password_reset.html', {'email': email})


def test(request):
    a = ['apple', 'pear', 'psjd', 'dfsf', 'dvsv']
    b = {'one': 'one', 'two': 'two', 'three': 'three'}

    return render(request, 'test.html', {'a': a, 'b': b})
