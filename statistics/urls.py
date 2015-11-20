#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from statistics import views

urlpatterns = patterns('',
    #  统计页首页  
    url(r'^statistics_list/(\d{1,6})/$', views.statistics_list),

)
