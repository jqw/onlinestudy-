from django.shortcuts import render
# 导入django视图
from django.views.generic import View


# Create your views here.
class CourseListView(View):
    def get(self, request):
        return render(request, 'course-list.html')
