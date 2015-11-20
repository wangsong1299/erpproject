#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from customer import views
from customer import tests

urlpatterns = patterns('',
    # 客户和应收列表  
    url(r'^customer_list/(\d{1,6})/$', views.customer_list),
   # 客户和应收搜索页结果
    url(r'^customer_search/(\d{1,6})/$', views.customer_search),
    # 供应商和应付列表  
    url(r'^supplier_list/(\d{1,6})/$', views.supplier_list),
   # 客户和应收搜索页结果
    url(r'^supplier_search/(\d{1,6})/$', views.supplier_search),


#api
    #根据piplineID得到内容
    url(r'^get_customerdetails_by_piplineID/$', views.get_customerdetails_by_piplineID),
    # 修改客户单
    url(r'^modify_customer/$', views.modify_customer),
    # 删除客户单
    url(r'^delete_customer/$', views.delete_customer),
    #有产品名得到客户ID
    url(r'^get_customerID_by_product/$', views.get_customerID_by_product),
    #有客户名得到客户ID
    url(r'^get_customerID_by_customer/$', views.get_customerID_by_customer),
  

    #根据piplineID得到内容
    url(r'^get_supplierdetails_by_piplineID/$', views.get_supplierdetails_by_piplineID),
    # 修改客户单
    url(r'^modify_supplier/$', views.modify_supplier),
    # 删除客户单
    url(r'^delete_supplier/$', views.delete_supplier),
    #有产品名得到客户ID
    url(r'^get_supplierID_by_material/$', views.get_supplierID_by_material),
    #有客户名得到客户ID
    url(r'^get_supplierID_by_supplier/$', views.get_supplierID_by_supplier),
  
  
 



)
