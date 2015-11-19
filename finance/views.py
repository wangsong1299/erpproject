#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from finance.models import Finance

def finance(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Finance.objects.all()
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
			a[i]=b
			i=i+1
		return render_to_response("finance_finance.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})


def search(request,productID):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Finance.objects.filter(productID=productID)
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
			a[i]=b
			i=i+1
		return render_to_response("finance_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})
	

#api
@csrf_exempt
def fill_finance(request):
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	col8 = request.POST.get('col8', None)
	try:
		q = Finance(delivery_time=col1,
				productID=col2,
				product_name=col3,
				order_amount=col4,	
				delivery_amount=col5,
				price=col6,
				total_fee=col7,
				notes=col8)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def get_details_by_ID(request):
	id = request.POST.get('id', None)
	try:
		r = Finance.objects.filter(id=id)[0]
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
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(b))

@csrf_exempt
def modify_finance(request):
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	col8 = request.POST.get('col8', None)
	id=request.POST.get('id', None)
	try:
		Finance.objects.filter(id=id).update(delivery_time=col1,productID=col2,product_name=col3,order_amount=col4,delivery_amount=col5,price=col6,total_fee=col7,notes=col8)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

#api
@csrf_exempt
def get_productID_by_product(request):
	product_name = request.POST.get('product_name', None)
	productID=Finance.objects.filter(product_name=product_name)[0].productID
	if(len(productID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(productID)

@csrf_exempt
def delete_finance(request):
	id=request.POST.get('id', None)
	try:
		Finance.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

