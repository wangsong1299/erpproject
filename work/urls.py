#! -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from work import views
from work import tests

urlpatterns = patterns('',
    # 产品追踪页 
    url(r'^tracking_list/(\d{1,6})/$', views.tracking_list),

    url(r'^tracking/(\d{1,6})/$', views.tracking),
    url(r'^tracking/c/(\d{1,6})/$', views.tracking_c),
    url(r'^tracking/p/(\d{1,6})/$', views.tracking_p),

#api
    url(r'^check_productID/$', views.check_productID),

    url(r'^get_details_by_ID/$', views.get_details_by_ID),

    url(r'^modify_tracking/$', views.modify_tracking),

    url(r'^get_productID_by_customer/$', views.get_productID_by_customer),
    url(r'^get_productID_by_product/$', views.get_productID_by_product),

    url(r'^delete_tracking/$', views.delete_tracking),

    #员工完成情况
    url(r'^worker_list/(\d{1,6})/$', views.worker_list),

     url(r'^get_workerdetails_by_ID/$', views.get_workerdetails_by_ID),
     url(r'^modify_worker/$', views.modify_worker),

    url(r'^delete_worker/$', views.delete_worker),

    url(r'^get_workerID_by_worker/$', views.get_workerID_by_worker),
    url(r'^get_workerID_by_product/$', views.get_workerID_by_product),

####
    #查询单个员工完成情况
    url(r'^worker/(\d{1,6})/$', views.worker_worker),
    url(r'^worker/c/(\d{1,6})/$', views.worker_c),
    url(r'^worker/p/(\d{1,6})/$', views.worker_p),




)
