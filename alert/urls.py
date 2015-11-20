#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from alert import views

urlpatterns = patterns('',
    #  统计页首页  
    url(r'^alert_list/(\d{1,6})/$', views.alert_list),

)
