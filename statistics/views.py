#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from storage.models import Storage,Storage_in,Storage_out,Storage_material
from django.utils.timezone import now, timedelta
from users.models import User
from finance.models import Finance
# Create your views here.
def get_statistics_list(records):	
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.product_name
		b[1]=r.material
		b[2]=r.daliao
		b[3]=r.size
		b[4]=r.id
		b[5]=r.material_ipt
		b[6]=r.material2
		b[7]=r.size2
		b[8]=r.material2_ipt
		b[9]=r.daliao2
		b[10]=r.wl_waleng
		b[11]=r.wl_waleng_ipt
		b[12]=r.wl_size
		b[13]=r.wl_amount
		b[14]=r.customer
		a[i]=b
		i=i+1
	return a

def statistics_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p9
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	start = now().date()
	end = start + timedelta(days=1)
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Process.objects.filter(create_time__range=(start, end))
		records=Process.objects.filter(create_time__range=(start, end)).order_by('-id')
		a=get_statistics_list(records)
		return render_to_response("statistics_statistics.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})

def get_delivery_list(records):
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.deliveryID
		b[1]=r.product_name
		b[2]=r.order_amount
		b[3]=r.delivery_amount
		b[4]=r.fee
		b[5]=r.id
		b[6]=r.delivery_time
		a[i]=b
		i=i+1
	return a

def get_finance_list(records):	
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.delivery_time
		b[1]=r.productID
		b[2]=r.product_name
		b[3]=r.order_amount
		b[4]=r.delivery_amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.notes
		b[8]=r.id
		b[9]=r.customer
		a[i]=b
		i=i+1
	return a

def statistics_search(request,year,month,day):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		date=year+"-"+month+"-"+day
		records=Process.objects.filter(create_time=date)
		if (len(records)==0):
			return render_to_response("statistics_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':records,'isValue':False})
		else:
			a=get_statistics_list(records)
			return render_to_response("statistics_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'isValue':True})

def time_search(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	return render_to_response("statistics_time_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name})

def time_search_d(request,start,end):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		startdate=start[0:4]+"-"+start[4:6]+"-"+start[6:8]
		enddate=end[0:4]+"-"+end[4:6]+"-"+end[6:8]
		records=Delivery.objects.filter(delivery_time__range=(startdate, enddate))
		if (len(records)==0):
			return render_to_response("statistics_time_search_d.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':records,'isValue':False})
		else:
			a=get_delivery_list(records)
			return render_to_response("statistics_time_search_d.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'isValue':True})

def time_search_f(request,start,end,customer):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		startdate=start[0:4]+"-"+start[4:6]+"-"+start[6:8]
		enddate=end[0:4]+"-"+end[4:6]+"-"+end[6:8]
		if customer and (str(customer)!='0'):
			records=Finance.objects.filter(delivery_time__range=(startdate, enddate)).filter(customer__contains=customer)
		else:
			records=Finance.objects.filter(delivery_time__range=(startdate, enddate))
		total=0
		for r in records:
			if(r.total_fee):
				total=total+float(r.total_fee)
		if (len(records)==0):
			return render_to_response("statistics_time_search_f.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':records,'isValue':False,'customer':customer})
		else:
			a=get_finance_list(records)
			return render_to_response("statistics_time_search_f.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'isValue':True,'total':total})
