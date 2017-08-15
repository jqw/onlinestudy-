from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from .models import CityDict, CourseOrg

from django.core.paginator import Paginator, PageNotAnInteger


# Create your views here.
class OrgListView(View):
    def get(self, request):
        # 机构类别,默认的情况
        orglist = CourseOrg.objects.all()
        # 结构排名
        hot_orglist = CourseOrg.objects.order_by('-click_nums')[0:3]

        # 搜索
        keywords = request.GET.get('keywords', '')
        if keywords:
            orglist = CourseOrg.objects.filter(Q(name__contains=keywords) | Q(desc__contains=keywords))

        # 根据类别进行筛选
        category = request.GET.get('ct', '')
        if category:
            orglist = CourseOrg.objects.filter(category=category)
        # 根据所在城市地区进行筛选
        city_id = request.GET.get('city', '')
        if city_id:
            orglist = CourseOrg.objects.filter(city_id=city_id)
        # 所有的城市
        citylist = CityDict.objects.all()

        # 根据字段进行排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                orglist = CourseOrg.objects.order_by('-students')
            elif sort == 'courses':
                orglist = CourseOrg.objects.order_by('-course_nums')
        try:
            page = request.GET.get('page', '1')
        # 实现分页
        except PageNotAnInteger as e:
            page = '1'
        paginator = Paginator(orglist, 5)
        # 判断页码是不是在有的范围中
        orgs = []
        page_range = []
        if int(page) <= paginator.num_pages:
            orgs = paginator.page(page)
            # 如果页码过多　首页　上一页　１２３４５　下一页　末页
            if paginator.num_pages > 5:
                if orgs.number == 1:
                    page_range = [1, 2, 3, 4, 5]
                elif orgs.number == 2:
                    page_range = [1, 2, 3, 4, 5]
                elif orgs.number == paginator.num_pages:
                    page_range = [orgs.number - 4, orgs.number - 3, orgs.number - 2, orgs.number - 1, orgs.number]
                elif orgs.number == paginator.num_pages - 1:
                    page_range = [orgs.number - 4, orgs.number - 3, orgs.number - 2, orgs.number - 1, orgs.number]
                else:
                    page_range = [orgs.number - 2, orgs.number - 1, orgs.number, orgs.number + 1, orgs.number + 2]
            else:
                for num in paginator.page_range:
                    page_range.append(num)

        return render(request, 'org-list.html',
                      {'orglist': orgs,
                       'hot_orglist': hot_orglist,
                       'city_id': city_id,
                       'citylist': citylist,
                       'category': category,
                       'paginator': paginator,
                       'page_range': page_range,
                       'sort': sort,
                       })

    def post(self, request):
        pass


# 机构详情
class OrgDetailView(View):
    def get(self, request, id):
        # 请求机构详情的名称
        list = CourseOrg.objects.filter(pk=id)
        # 全部课程
        listCourse = list[0].course_set.all()[0:3]
        # 机构教师
        # teacher = list[0].teacher_set.all()[0]
        current = '1'
        context = {'title': '机构详情', 'current': current, 'orgid': id, 'org': list[0], 'listCourse': listCourse}
        return render(request, 'org-detail-homepage.html', context)


# 机构课程
class OrgCourseView(View):
    def get(self, request, id):
        list = CourseOrg.objects.filter(pk=id)
        listCourse = list[0].course_set.all()[0:4]
        current = '2'
        context = {'title': '机构课程', 'current': current, 'listCourse': listCourse}
        return render(request, 'org-detail-course.html', context)


# 机构介绍
class OrgDescView(View):
    def get(self, request, id):
        # org = CourseOrg.objects.filter(pk=id)[0]
        current = '3'
        context = {'title': '机构介绍', 'current': current}
        return render(request, 'org-detail-desc.html', context)


class OrgTeachersView(View):
    def get(self, request):
        #org = CourseOrg.objects.filter(pk=id)[0]
        #teacherlist = org.teacher_set.all()
        current = '4'
        context = {'title': '机构讲师', 'current': current}
        return render(request, 'org-detail-teachers.html', context)


class TeacherListView(View):
    def get(self, request):
        return render(request, 'teachers-list.html')
