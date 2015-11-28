#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from purchase import views

urlpatterns = patterns('',
    # 采购单首页
    url(r'^purchase_list/(\d{1,6})/$', views.purchase_list),

    url(r'^choice/$', views.choice),
     # 采购单填写页  
    url(r'^fill/(\d{1,6})/$', views.fill),
    # 采购单历史查询 
    url(r'^search/(\d{1,6})/$', views.search),
 


 #api
    url(r'^get_productID_by_product/$', views.get_productID_by_product),
    url(r'^get_productID_by_customer/$', views.get_productID_by_customer),
    url(r'^get_productID_by_productID/$', views.get_productID_by_productID),
 
    url(r'^fill_single/$', views.fill_single),
    url(r'^fill_multiple/$', views.fill_multiple),
    url(r'^fill_multiple_list/$', views.fill_multiple_list),
 
    url(r'^delete_single/$', views.delete_single),
    url(r'^delete_multiple/$', views.delete_multiple),
 
    url(r'^modify_single/$', views.modify_single),
    url(r'^modify_multiple/$', views.modify_multiple),
 


)
