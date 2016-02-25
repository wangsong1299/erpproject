#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from finance.models import Finance
from users.models import User

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

def finance_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p4
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Finance.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Finance.objects.all().order_by('-id')
				a=get_finance_list(records)
			else:
				records=Finance.objects.all().order_by('-id')[0:10]
				a=get_finance_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Finance.objects.all().order_by('-id')[last:]
				a=get_finance_list(records)
			else:
				first=int(num-1)*10
				records=Finance.objects.all().order_by('-id')[first:int(first+10)]
				a=get_finance_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		jc=False
		return render_to_response("finance_finance.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click),'jc':json.dumps(jc)})

def finance_p(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		product_name=Finance.objects.filter(id=id)[0].product_name
		records=Finance.objects.filter(product_name=product_name)
		a=get_finance_list(records)
		pre_click=False
		later_click=False
		jc=True
		return render_to_response("finance_finance.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click),'jc':json.dumps(jc)})

def finance_c(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		customer=Finance.objects.filter(id=id)[0].customer
		records=Finance.objects.filter(customer=customer)
		a=get_finance_list(records)
		pre_click=False
		later_click=False
		jc=True
		return render_to_response("finance_finance.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click),'jc':json.dumps(jc)})


def search(request,financeID):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		product_name=Finance.objects.filter(financeID=financeID)[0].product_name
		records=Finance.objects.filter(product_name=product_name)
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
	col9 = request.POST.get('col9', None)
	try:
		q = Finance(delivery_time=col1,
				productID=col2,
				product_name=col3,
				order_amount=col4,	
				delivery_amount=col5,
				price=col6,
				total_fee=col7,
				notes=col8,
				customer=col9)
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
		b[9]=r.customer
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
	col9 = request.POST.get('col9', None)
	id=request.POST.get('id', None)
	try:
		Finance.objects.filter(id=id).update(delivery_time=col1,productID=col2,product_name=col3,order_amount=col4,delivery_amount=col5,price=col6,total_fee=col7,notes=col8,customer=col9)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

#api
@csrf_exempt
def get_productID_by_product(request):
	product_name = request.POST.get('finance_search', None)
	r=Finance.objects.filter(product_name=product_name)
	print r
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)
		
@csrf_exempt
def get_productID_by_customer(request):
	customer = request.POST.get('finance_search', None)
	r=Finance.objects.filter(customer=customer)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)


@csrf_exempt
def delete_finance(request):
	id=request.POST.get('id', None)
	try:
		Finance.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

