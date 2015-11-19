#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from alert import views

urlpatterns = patterns('',
    #  统计页首页  
    url(r'^alert/$', views.alert),

)
