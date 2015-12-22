#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from sales import views
from sales import tests

urlpatterns = patterns('',
    #报价单
    # 报价单列表 
    url(r'^quotation_list/(\d{1,6})/$', views.quotation_list),
    # 新建报价单
    url(r'^quotation_new/$', views.quotation_new),
    # 报价单单页（显示）
    url(r'^quotation/(\d{1,6})/$', views.quotation),
    # 报价单单页（修改）
    url(r'^quotation_modify/(\d{1,6})/$', views.quotation_modify),
#api
    #写入报价单
    url(r'^fill_quotation/$', views.fill_quotation),
    #修改报价单
    url(r'^modify_quotation/$', views.modify_quotation),
    #删除报价单
    url(r'^delete_quotation/$', views.delete_quotation),
    #有产品名得到客户ID
    url(r'^get_quotationID_by_product/$', views.get_quotationID_by_product),
    #有客户名得到客户ID
    url(r'^get_quotationID_by_customer/$', views.get_quotationID_by_customer),
     # 报价单搜索页
    url(r'^quotation/c/(\d{1,6})/$', views.quotation_c),
    url(r'^quotation/p/(\d{1,6})/$', views.quotation_p),
##########################################################

  #订单
    # 新建报价单  
    url(r'^order_list/(\d{1,6})/$', views.order_list),
    # 新建报价单  
    url(r'^order_new/$', views.order_new),
    # 报价单单页（显示）
    url(r'^order/(\d{1,6})/$', views.order),
    # 报价单单页（修改）
    url(r'^order_modify/(\d{1,6})/$', views.order_modify),
#api
    url(r'^fill_order/$', views.fill_order),
    url(r'^modify_order/$', views.modify_order),
    #删除订单
    url(r'^delete_order/$', views.delete_order),
    #有产品名得到客户ID
    url(r'^get_orderID_by_product/$', views.get_orderID_by_product),
    #有客户名得到客户ID
    url(r'^get_orderID_by_customer/$', views.get_orderID_by_customer),
    url(r'^order/c/(\d{1,6})/$', views.order_c),
    url(r'^order/p/(\d{1,6})/$', views.order_p),


##########################################################
  #送货单
    # 送货单列表  
    url(r'^delivery_list/(\d{1,6})/$', views.delivery_list),
    # 新建送货单  
    url(r'^delivery_new/(\d{1})/$', views.delivery_new),
    # 报价单单页（显示）
    url(r'^delivery/(\d{1,6})/$', views.delivery),
    # 报价单单页（修改）
    url(r'^delivery_modify/(\d{1,6})/$', views.delivery_modify),
#api
    url(r'^fill_delivery/$', views.fill_delivery),
    url(r'^fill_delivery_2/$', views.fill_delivery_2),
    url(r'^fill_delivery_3/$', views.fill_delivery_3),

   url(r'^modify_delivery/$', views.modify_delivery),
   url(r'^modify_delivery_2/$', views.modify_delivery_2),
   url(r'^modify_delivery_3/$', views.modify_delivery_3),


   url(r'^delete_delivery/$', views.delete_delivery),
    #有客户名得到客户ID
    url(r'^get_deliveryID_by_product/$', views.get_deliveryID_by_product),
    url(r'^get_deliveryID_by_deliveryID/$', views.get_deliveryID_by_deliveryID),

#根据产品号自动填充
    url(r'^get_details_from_order/$', views.get_details_from_order),
    url(r'^delivery/p/(\d{1,6})/$', views.delivery_p),

 ##########################################################
  #施工单
    # 施工单  
    url(r'^process_list/(\d{1,6})/$', views.process_list),
    # 新建施工单  
    url(r'^process_new/$', views.process_new),
    # 施工单单页（显示）
    url(r'^process/(\d{1,6})/$', views.process),
    # 施工单单页（修改）
    url(r'^process_modify/(\d{1,6})/$', views.process_modify),

    # 施工单单日汇总
    url(r'^process_search/$', views.process_search),
    url(r'^process_search/(\d{4})/(\d{1,2})/(\d{1,2})/$', views.process_search_date),

    url(r'^fill_process/$', views.fill_process),
    url(r'^modify_process/$', views.modify_process),
    url(r'^delete_process/$', views.delete_process),
    url(r'^get_processID_by_customer/$', views.get_processID_by_customer),
    url(r'^get_processID_by_product/$', views.get_processID_by_product),
    url(r'^check_img/$', views.check_img),

    url(r'^process/c/(\d{1,6})/$', views.process_c),
    url(r'^process/p/(\d{1,6})/$', views.process_p),

 ##########################################################
  #成本单
    # 新建成本单  
    url(r'^cost_list/(\d{1,6})/$', views.cost_list),

    url(r'^get_details_from_process/$', views.get_details_from_process),

    # 新建成本单  
    url(r'^cost_new/$', views.cost_new),

    # 施工单单页（显示）
    url(r'^cost/(\d{1,6})/$', views.cost),
    # 施工单单页（修改）
    url(r'^cost_modify/(\d{1,6})/$', views.cost_modify),

 	url(r'^fill_cost/$', views.fill_cost),
    url(r'^modify_cost/$', views.modify_cost),
    url(r'^delete_cost/$', views.delete_cost),
    url(r'^get_costID_by_customer/$', views.get_costID_by_customer),
    url(r'^get_costID_by_product/$', views.get_costID_by_product),
    url(r'^cost/c/(\d{1,6})/$', views.cost_c),
    url(r'^cost/p/(\d{1,6})/$', views.cost_p),

)
