#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from statistics import views

urlpatterns = patterns('',
    #  统计页首页  
    url(r'^statistics_list/(\d{1,6})/$', views.statistics_list),
    url(r'^statistics_search/(\d{4})/(\d{1,2})/(\d{1,2})/$', views.statistics_search),

)
