#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from finance import views

urlpatterns = patterns('',
    # 财务首页  
    url(r'^finance_list/(\d{1,6})/$', views.finance_list),
    #财务搜索结果页
    url(r'^search/(\d{1,6})/$', views.search),
    url(r'^finance/p/(\d{1,6})/$', views.finance_p),
    url(r'^finance/c/(\d{1,6})/$', views.finance_c),

#api
    # 填写对账单
    url(r'^fill_finance/$', views.fill_finance),
    #根据piplineID得到内容
    url(r'^get_details_by_ID/$', views.get_details_by_ID),
    # 修改对账单
    url(r'^modify_finance/$', views.modify_finance),
    #有产品名得到产品ID
    url(r'^get_productID_by_product/$', views.get_productID_by_product),
    url(r'^get_productID_by_customer/$', views.get_productID_by_customer),
    # 删除对账单
    url(r'^delete_finance/$', views.delete_finance),


)
