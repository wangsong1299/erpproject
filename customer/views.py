#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from purchase.models import Purchase_single,Purchase_multiple
from customer.models import Customer,Supplier

def get_customer_list(records):	
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.customers
		b[1]=r.contacts
		b[2]=r.contacts_phone
		b[3]=r.product_name
		b[4]=r.amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.create_time
		b[8]=r.notes
		b[9]=r.id
		a[i]=b
		i=i+1
	return a

def customer_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Customer.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Customer.objects.all().order_by('-id')
				a=get_customer_list(records)
			else:
				records=Customer.objects.all().order_by('-id')[0:10]
				a=get_customer_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Customer.objects.all().order_by('-id')[last:]
				a=get_customer_list(records)
			else:
				first=int(num-1)*10
				records=Customer.objects.all().order_by('-id')[first:int(first+10)]
				a=get_customer_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("customer_customer.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})


def customer_search(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		r=Customer.objects.filter(id=id)[0]
		b={}
		b[0]=r.customers
		b[1]=r.contacts
		b[2]=r.contacts_phone
		b[3]=r.product_name
		b[4]=r.amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.create_time
		b[8]=r.notes
		b[9]=r.id
		return render_to_response("customer_customer_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"record":b})

def get_supplier_list(records):	
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.suppliers
		b[1]=r.contacts
		b[2]=r.contacts_phone
		b[3]=r.material_name
		b[4]=r.amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.create_time.strftime('%Y-%m-%d')
		b[8]=r.notes
		b[9]=r.id
		a[i]=b
		i=i+1
	return a

def supplier_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Supplier.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Supplier.objects.all().order_by('-id')
				a=get_supplier_list(records)
			else:
				records=Supplier.objects.all().order_by('-id')[0:10]
				a=get_supplier_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Supplier.objects.all().order_by('-id')[last:]
				a=get_supplier_list(records)
			else:
				first=int(num-1)*10
				records=Supplier.objects.all().order_by('-id')[first:int(first+10)]
				a=get_supplier_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("customer_supplier.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})


def supplier_search(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		r=Supplier.objects.filter(id=id)[0]
		b={}
		b[0]=r.suppliers
		b[1]=r.contacts
		b[2]=r.contacts_phone
		b[3]=r.material_name
		b[4]=r.amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.create_time.strftime('%Y-%m-%d')
		b[8]=r.notes
		b[9]=r.id
		return render_to_response("customer_supplier_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"record":b})



#api
@csrf_exempt
def get_customerdetails_by_piplineID(request):
	id = request.POST.get('id', None)
	try:
		r = Customer.objects.filter(id=id)[0]
		b={}
		b[0]=r.customers
		b[1]=r.contacts
		b[2]=r.contacts_phone
		b[3]=r.product_name
		b[4]=r.amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.create_time
		b[8]=r.notes
		b[9]=r.id
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(b))


@csrf_exempt
def modify_customer(request):
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
		Customer.objects.filter(id=id).update(customers=col1,contacts=col2,contacts_phone=col3,product_name=col4,amount=col5,price=col6,total_fee=col7,create_time=col8,notes=col9)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_customer(request):
	id=request.POST.get('id', None)
	try:
		Customer.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

#api
@csrf_exempt
def get_customerID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Customer.objects.filter(product_name=product_name)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)

#api
@csrf_exempt
def get_customerID_by_customer(request):
	cumtomer = request.POST.get('customer', None)
	r=Customer.objects.filter(customers=cumtomer)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)

#供应商
#api
@csrf_exempt
def get_supplierdetails_by_piplineID(request):
	id = request.POST.get('id', None)
	try:
		r = Supplier.objects.filter(id=id)[0]
		b={}
		b[0]=r.suppliers
		b[1]=r.contacts
		b[2]=r.contacts_phone
		b[3]=r.material_name
		b[4]=r.amount
		b[5]=r.price
		b[6]=r.total_fee
		b[7]=r.create_time.strftime('%Y-%m-%d')
		b[8]=r.notes
		b[9]=r.id
		print b
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(b))


@csrf_exempt
def modify_supplier(request):
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
		Supplier.objects.filter(id=id).update(suppliers=col1,contacts=col2,contacts_phone=col3,material_name=col4,amount=col5,price=col6,total_fee=col7,create_time=col8,notes=col9)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_supplier(request):
	id=request.POST.get('id', None)
	try:
		Supplier.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

#api
@csrf_exempt
def get_supplierID_by_material(request):
	material_name = request.POST.get('material_name', None)
	r = Supplier.objects.filter(material_name=material_name)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)
#api
@csrf_exempt
def get_supplierID_by_supplier(request):
	suppliers = request.POST.get('supplier', None)
	r = Supplier.objects.filter(suppliers=suppliers)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)




