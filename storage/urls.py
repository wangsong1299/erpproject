#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from storage import views
from storage import tests

urlpatterns = patterns('',
    # 库存
    url(r'^storage_list/(\d{1,6})/$', views.storage_list),
    url(r'^storage/(\d{1,6})/$', views.storage),
    url(r'^storage/c/(\d{1,6})/$', views.storage_c),
    url(r'^storage/p/(\d{1,6})/$', views.storage_p),

    #原料仓库
    url(r'^storage_material_list/(\d{1,6})/$', views.storage_material_list),
    url(r'^storage_material/(\d{1,6})/$', views.storage_material),
  

  #api
    url(r'^fill_storage_in/$', views.fill_storage_in),
    url(r'^fill_storage_out/$', views.fill_storage_out),
 
    url(r'^modify_storage/$', views.modify_storage),
    url(r'^delete_storage/$', views.delete_storage),

    #有产品名得到客户ID
    url(r'^get_storageID_by_product/$', views.get_storageID_by_product),
    #有客户名得到客户ID
    url(r'^get_storageID_by_customer/$', views.get_storageID_by_customer),
 
#入库单
    #入库
    url(r'^storage_in_list/(\d{1,6})/$', views.storage_in_list),
    url(r'^storage_in/new/$', views.storage_in_new),
    url(r'^storage_in/(\d{1,6})/$', views.storage_in_show),
    url(r'^storage_in/p/(\d{1,6})/$', views.storage_in_p),


    url(r'^modify_storage_in/$', views.modify_storage_in),
    url(r'^delete_storage_in/$', views.delete_storage_in),
    url(r'^get_storage_inID_by_product/$', views.get_storage_inID_by_product),
#出库单
    #出库
    url(r'^storage_out_list/(\d{1,6})/$', views.storage_out_list),
    url(r'^storage_out/new/$', views.storage_out_new),
    url(r'^storage_out/(\d{1,6})/$', views.storage_out_show),
    url(r'^storage_out/p/(\d{1,6})/$', views.storage_out_p),
 
    url(r'^modify_storage_out/$', views.modify_storage_out),
    url(r'^delete_storage_out/$', views.delete_storage_out),
    url(r'^get_storage_outID_by_product/$', views.get_storage_outID_by_product),

    url(r'^modify_material/$', views.modify_material),
    url(r'^delete_material/$', views.delete_material),


   url(r'^get_details_by_material/$', views.get_details_by_material),


#####
   url(r'^get_storagedetails_by_piplineID/$', views.get_storagedetails_by_piplineID),
   url(r'^get_materialdetails_by_piplineID/$', views.get_materialdetails_by_piplineID),

)
