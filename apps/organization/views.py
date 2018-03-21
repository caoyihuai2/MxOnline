# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class OrgView(View):
    """
    课程机构列表首页
    """
    def get(self, request):
        return render(request, "org-list.html")
