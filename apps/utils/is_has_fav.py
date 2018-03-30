# -*- coding:utf-8 -*-
from operation.models import UserFavorite

__author__ = 'cao.yh'
__date__ = '2018/3/26 下午5:07'


def has_fav(user, fav_id, fav_type):
    if user.is_authenticated():
        if UserFavorite.objects.get(user=user, fav_id=fav_id, fav_type=fav_type):
            return True
        else:
            return False
    else:
        return False
