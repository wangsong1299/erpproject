#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from users import views
from users import tests

urlpatterns = patterns('',
    # 用户列表   
    url(r'^list/(\d{1,6})/$', views.list),
    # 用户分配
    url(r'^new/$', views.new),
    url(r'^(\d{1,6})/$', views.user),

    #api
    #登录
    url(r'^signin/$', views.signin),
    #注册
    url(r'^signup/$', views.signup),
    url(r'^delete_user/$', views.delete_user),
    url(r'^modify_user/$', views.modify_user),

    url(r'^get_id_by_username/$', views.get_id_by_username),

)

