from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import index,logout,barcode,upload_iframe,upload_show
from view import api_test,get_process_info,count_work,login_in,modify_password,upload,get_test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'erpproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',index),
    url(r'^logout/$',logout),

    url(r'^users/', include('users.urls')),
    url(r'^sales/', include('sales.urls')),
    url(r'^work/', include('work.urls')),
    url(r'^purchase/', include('purchase.urls')),
    url(r'^storage/', include('storage.urls')),
    url(r'^finance/', include('finance.urls')),
    url(r'^customer/', include('customer.urls')),
    url(r'^statistics/', include('statistics.urls')),
    url(r'^alert/', include('alert.urls')),


    url(r'^api_test/$',api_test),
    url(r'^upload/$',upload),

    url(r'^barcode/(\d{1,12})/$',barcode),
    url(r'^upload_iframe/(\d{1,12})/$',upload_iframe),
    url(r'^upload_show/(\d{1,12})/$',upload_show),

#api
    url(r'^get_process_info/$',get_process_info),
    url(r'^count_work/$',count_work),
    url(r'^login_in/$',login_in),
    url(r'^modify_password/$',modify_password),
    url(r'^get_test/$',get_test),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
