from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
from operation.forms import UserAskForm

# 用户添加咨询
class UserAskView(View):
    def post(self, request):
        useraskform = UserAskForm(request.POST)
        if useraskform.is_valid():
            # 验证合法
            # 默认是commit=true
            user_ask = useraskform.save(commit=True)
            return JsonResponse({'status': 'success'})
        else:
            msg = useraskform.errors
            return JsonResponse({'status': 'fail', 'msg': str(useraskform.errors)})

