# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.views.generic.base import View

from organization.models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表首页
    """
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_citys = CityDict.objects.all()
        org_nums = all_orgs.count()

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
        })
