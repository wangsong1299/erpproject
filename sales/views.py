#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from storage.models import Storage
from finance.models import Finance
from work.models import Tracking
from customer.models import Customer,Supplier
#报价单列表
def get_quotation_list(records):
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.customer
		b[1]=r.product_name
		b[2]=r.create_time.strftime('%Y-%m-%d')
		b[3]=r.total_fee
		b[4]=r.id
		a[i]=b
		i=i+1
	return a

def quotation_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	quotation=True
	order=False
	delivery=False
	process=False
	cost=False
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Quotation.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Quotation.objects.all().order_by('-id')
				a=get_quotation_list(records)
			else:
				records=Quotation.objects.all().order_by('-id')[0:10]
				a=get_quotation_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Quotation.objects.all().order_by('-id')[last:]
				a=get_quotation_list(records)
			else:
				first=int(num)*10
				records=Quotation.objects.all().order_by('-id')[first:int(first+10)]
				a=get_quotation_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("sales_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,"quotation":quotation,'order':order,'delivery':delivery,'process':process,'cost':cost,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})



#新建报价单
def quotation_new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		return render_to_response("sales_quotation_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name})

#报价单单页
def quotation(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		quotation_show=True
		quotation_modify=False
		r=Quotation.objects.filter(id=id)[0]
		b={}
		b[0]=r.customer
		b[1]=r.product_name
		b[2]=r.create_time
		b[3]=r.contacts
		b[4]=r.contacts_phone
		b[5]=r.material_price
		b[6]=r.size_price
		b[7]=r.wl_material_price
		b[8]=r.amount_price
		b[9]=r.print_fee_price
		b[10]=r.print_color_price
		b[11]=r.print_parts_price
		b[12]=r.surface_price
		b[13]=r.tangjin_price
		b[14]=r.safen_price
		b[15]=r.packing_box_price
		b[16]=r.packing_fee_price
		b[17]=r.transportation_fee_price
		b[18]=r.material
		b[19]=r.size
		b[20]=r.wl_material
		b[21]=r.amount
		b[22]=r.print_fee
		b[23]=r.print_color
		b[24]=r.print_parts
		b[25]=r.surface
		b[26]=r.tangjin
		b[27]=r.safen
		b[28]=r.packing_box
		b[29]=r.packing_fee
		b[30]=r.transportation_fee
		b[31]=r.total_fee
		c={}
		c[0]=r.size
		c[1]=r.amount
		c[2]=r.surface
		c[3]=r.id
		return render_to_response("sales_quotation.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b,'choice':json.dumps(c),'quotation_show':json.dumps(quotation_show),'quotation_modify':json.dumps(quotation_modify)})
#api


#报价单单页
def quotation_modify(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		quotation_show=False
		quotation_modify=True
		r=Quotation.objects.filter(id=id)[0]
		b={}
		b[0]=r.customer
		b[1]=r.product_name
		b[2]=r.create_time
		b[3]=r.contacts
		b[4]=r.contacts_phone
		b[5]=r.material_price
		b[6]=r.size_price
		b[7]=r.wl_material_price
		b[8]=r.amount_price
		b[9]=r.print_fee_price
		b[10]=r.print_color_price
		b[11]=r.print_parts_price
		b[12]=r.surface_price
		b[13]=r.tangjin_price
		b[14]=r.safen_price
		b[15]=r.packing_box_price
		b[16]=r.packing_fee_price
		b[17]=r.transportation_fee_price
		b[18]=r.material
		b[19]=r.size
		b[20]=r.wl_material
		b[21]=r.amount
		b[22]=r.print_fee
		b[23]=r.print_color
		b[24]=r.print_parts
		b[25]=r.surface
		b[26]=r.tangjin
		b[27]=r.safen
		b[28]=r.packing_box
		b[29]=r.packing_fee
		b[30]=r.transportation_fee
		b[31]=r.total_fee
		c={}
		c[0]=r.size
		c[1]=r.amount
		c[2]=r.surface
		c[3]=r.id
		return render_to_response("sales_quotation.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b,'choice':json.dumps(c),'quotation_show':json.dumps(quotation_show),'quotation_modify':json.dumps(quotation_modify)})
#api
@csrf_exempt
def fill_quotation(request):
	customer = request.POST.get('customer', None)
	product_name = request.POST.get('product_name', None)
	create_time = request.POST.get('create_time', None)
	contacts = request.POST.get('contacts', None)
	contacts_phone = request.POST.get('contacts_phone', None)

	total_fee = request.POST.get('total_fee', None)

	material_price = request.POST.get('material_price', None)
	size_price = request.POST.get('size_price', None)
	wl_material_price=request.POST.get('wl_material_price', None)
	amount_price = request.POST.get('amount_price', None)
	print_fee_price = request.POST.get('print_fee_price', None)
	print_color_price = request.POST.get('print_color_price', None)
	print_parts_price = request.POST.get('print_parts_price', None)
	surface_price = request.POST.get('surface_price', None)
	tangjin_price = request.POST.get('tangjin_price', None)
	safen_price = request.POST.get('safen_price', None)
	packing_fee_price = request.POST.get('packing_fee_price', None)
	packing_box_price = request.POST.get('packing_box_price', None)
	transportation_fee_price = request.POST.get('transportation_fee_price', None)

	material = request.POST.get('material', None)
	size = request.POST.get('size', None)
	wl_material=request.POST.get('wl_material', None)
	amount = request.POST.get('amount', None)
	print_fee = request.POST.get('print_fee', None)
	print_color = request.POST.get('print_color', None)
	print_parts = request.POST.get('print_parts', None)
	surface = request.POST.get('surface', None)
	tangjin = request.POST.get('tangjin', None)
	safen = request.POST.get('safen', None)
	packing_fee = request.POST.get('packing_fee', None)
	packing_box = request.POST.get('packing_box', None)
	transportation_fee = request.POST.get('transportation_fee', None)

	try:
		q=Quotation(customer = customer,
                product_name = product_name,
                create_time = create_time,
                contacts=contacts,
                contacts_phone=contacts_phone,
                total_fee=total_fee,
                material_price=material_price,
                size_price=size_price,
                wl_material_price=wl_material_price,
                amount_price=amount_price,
                print_fee_price=print_fee_price,
                print_color_price=print_color_price,
                print_parts_price=print_parts_price,
                surface_price=surface_price,
                tangjin_price=tangjin_price,
                safen_price=safen_price,
                packing_fee_price=packing_fee_price,
                packing_box_price=packing_box_price,
                transportation_fee_price=transportation_fee_price,
                material=material,
                size=size,
                wl_material=wl_material,
                amount=amount,
                print_fee=print_fee,
                print_color=print_color,
                print_parts=print_parts,
                surface=surface,
                tangjin=tangjin,
                safen=safen,
                packing_fee=packing_fee,
                packing_box=packing_box,
                transportation_fee=transportation_fee)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	
	return HttpResponse(json.dumps(1))


#修改报价单
@csrf_exempt
def modify_quotation(request):
	id= request.POST.get('id', None)

	customer = request.POST.get('customer', None)
	product_name = request.POST.get('product_name', None)
	create_time = request.POST.get('create_time', None)
	contacts = request.POST.get('contacts', None)
	contacts_phone = request.POST.get('contacts_phone', None)

	total_fee = request.POST.get('total_fee', None)

	material_price = request.POST.get('material_price', None)
	size_price = request.POST.get('size_price', None)
	wl_material_price=request.POST.get('wl_material_price', None)
	amount_price = request.POST.get('amount_price', None)
	print_fee_price = request.POST.get('print_fee_price', None)
	print_color_price = request.POST.get('print_color_price', None)
	print_parts_price = request.POST.get('print_parts_price', None)
	surface_price = request.POST.get('surface_price', None)
	tangjin_price = request.POST.get('tangjin_price', None)
	safen_price = request.POST.get('safen_price', None)
	packing_fee_price = request.POST.get('packing_fee_price', None)
	packing_box_price = request.POST.get('packing_box_price', None)
	transportation_fee_price = request.POST.get('transportation_fee_price', None)

	material = request.POST.get('material', None)
	size = request.POST.get('size', None)
	wl_material=request.POST.get('wl_material', None)
	amount = request.POST.get('amount', None)
	print_fee = request.POST.get('print_fee', None)
	print_color = request.POST.get('print_color', None)
	print_parts = request.POST.get('print_parts', None)
	surface = request.POST.get('surface', None)
	tangjin = request.POST.get('tangjin', None)
	safen = request.POST.get('safen', None)
	packing_fee = request.POST.get('packing_fee', None)
	packing_box = request.POST.get('packing_box', None)
	transportation_fee = request.POST.get('transportation_fee', None)

	try:
		Quotation.objects.filter(id=id).update(customer = customer,
                product_name = product_name,
                create_time = create_time,
                contacts=contacts,
                contacts_phone=contacts_phone,
                total_fee=total_fee,
                material_price=material_price,
                size_price=size_price,
                wl_material_price=wl_material_price,
                amount_price=amount_price,
                print_fee_price=print_fee_price,
                print_color_price=print_color_price,
                print_parts_price=print_parts_price,
                surface_price=surface_price,
                tangjin_price=tangjin_price,
                safen_price=safen_price,
                packing_fee_price=packing_fee_price,
                packing_box_price=packing_box_price,
                transportation_fee_price=transportation_fee_price,
                material=material,
                size=size,
                wl_material=wl_material,
                amount=amount,
                print_fee=print_fee,
                print_color=print_color,
                print_parts=print_parts,
                surface=surface,
                tangjin=tangjin,
                safen=safen,
                packing_fee=packing_fee,
                packing_box=packing_box,
                transportation_fee=transportation_fee)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	
	return HttpResponse(json.dumps(1))

#删除报价单
@csrf_exempt
def delete_quotation(request):
	id = request.POST.get('id', None)
	try:
		Quotation.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))


#api
@csrf_exempt
def get_quotationID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Quotation.objects.filter(product_name=product_name)
	if r:
		quotationID=r[0].id
		return HttpResponse(quotationID)
	else:
		return HttpResponse(0)
#api
@csrf_exempt
def get_quotationID_by_customer(request):
	customer = request.POST.get('customer', None)
	r=Quotation.objects.filter(customer=customer)
	if r:
		quotationID=r[0].id
		return HttpResponse(quotationID)
	else:
		return HttpResponse(0)

##################################################################################


#订单
#订单单列表
def get_order_list(records):
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.customer
		b[1]=r.product_name
		b[2]=r.create_time
		b[3]=r.productID
		b[4]=r.id
		b[5]=r.orderID
		a[i]=b
		i=i+1
	return a

def order_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	quotation=False
	order=True
	delivery=False
	process=False
	cost=False
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Order.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Order.objects.all().order_by('-id')
				a=get_order_list(records)
			else:
				records=Order.objects.all().order_by('-id')[0:10]
				a=get_order_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Order.objects.all().order_by('-id')[last:]
				a=get_order_list(records)
			else:
				first=int(num)*10
				records=Order.objects.all().order_by('-id')[first:int(first+10)]
				a=get_order_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("sales_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,"quotation":quotation,'order':order,'delivery':delivery,'process':process,'cost':cost,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})

def order_new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Order.objects.all().order_by('-id')
		if records:
			orderID=int(records[0].orderID)+1
		else:
			orderID=1
		return render_to_response("sales_order_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'orderID':orderID})

#报价单单页
def order(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		order_show=True
		order_modify=False
		records=Order.objects.filter(orderID=id)
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.customer
			b[1]=r.contacts
			b[2]=r.contacts_phone
			b[3]=r.fax
			b[4]=r.qq
			b[5]=r.create_time
			b[6]=r.product_name
			b[7]=r.productID
			b[8]=r.amount
			b[9]=r.price
			b[10]=r.fee
			b[11]=r.edition_fee
			b[12]=r.total_fee
			b[13]=r.deadline
			b[14]=r.feilin
			b[15]=r.material
			b[16]=r.size
			b[17]=r.surface
			b[18]=r.wl_material
			b[19]=r.wl_kind
			b[20]=r.mould
			b[21]=r.notes
			b[22]=r.delivery_address
			b[23]=r.call
			b[24]=r.productID2
			b[25]=int(i+1)
			b[26]=r.id
			b[27]=r.orderID
			a[i]=b
			i=i+1
		return render_to_response("sales_order.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'order_show':json.dumps(order_show),'order_modify':json.dumps(order_modify),'length':json.dumps(i)})
#api
#报价单单页
def order_modify(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		order_show=False
		order_modify=True
		records=Order.objects.filter(orderID=id)
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.customer
			b[1]=r.contacts
			b[2]=r.contacts_phone
			b[3]=r.fax
			b[4]=r.qq
			b[5]=r.create_time
			b[6]=r.product_name
			b[7]=r.productID
			b[8]=r.amount
			b[9]=r.price
			b[10]=r.fee
			b[11]=r.edition_fee
			b[12]=r.total_fee
			b[13]=r.deadline
			b[14]=r.feilin
			b[15]=r.material
			b[16]=r.size
			b[17]=r.surface
			b[18]=r.wl_material
			b[19]=r.wl_kind
			b[20]=r.mould
			b[21]=r.notes
			b[22]=r.delivery_address
			b[23]=r.call
			b[24]=r.productID2
			b[25]=int(i+1)
			b[26]=r.id
			b[27]=r.orderID
			a[i]=b
			i=i+1
		return render_to_response("sales_order.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'order_show':json.dumps(order_show),'order_modify':json.dumps(order_modify),'length':json.dumps(i)})
#api

@csrf_exempt
def fill_order(request):
	productID = request.POST.get('productID', None)
	customer = request.POST.get('customer', None)
	contacts = request.POST.get('contacts', None)
	contacts_phone = request.POST.get('contacts_phone', None)
	fax = request.POST.get('fax', None)		
	qq = request.POST.get('qq', None)
	create_time = request.POST.get('create_time', None)
	product_name = request.POST.get('product_name', None)
	amount = request.POST.get('amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	edition_fee = request.POST.get('edition_fee', None)
	total_fee = request.POST.get('total_fee', None)
	deadline = request.POST.get('deadline', None)
	feilin = request.POST.get('feilin', None)
	material = request.POST.get('material', None)
	size = request.POST.get('size', None)
	surface = request.POST.get('surface', None)
	wl_material = request.POST.get('wl_material', None)
	wl_kind = request.POST.get('wl_kind', None)
	mould = request.POST.get('mould', None)
	notes = request.POST.get('notes', None)	
	delivery_address = request.POST.get('delivery_address', None)
	call = request.POST.get('call', None)
	productID2 = request.POST.get('productID2', None)
	orderID = request.POST.get('orderID', None)
	
	try:
		q = Order(productID=productID,
				customer = customer,
				contacts=contacts,
				contacts_phone=contacts_phone,
				fax = fax,
				qq=qq,
				create_time=create_time,
				product_name=product_name,				
				amount = amount,
				price=price,
				fee = fee,
				edition_fee=edition_fee,
				total_fee = total_fee,
				deadline=deadline,
				feilin = feilin,
				material = material,
				size = size,
				surface=surface,
				wl_material=wl_material,
				wl_kind=wl_kind,
				mould=mould,      
				notes=notes,
				delivery_address=delivery_address,
				call=call,
				productID2=productID2,
				orderID=orderID)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	try:
		q = Customer(productID=productID,
				customers = customer,
				contacts=contacts,
				contacts_phone=contacts_phone,
				product_name=product_name,				
				amount = amount,
				price=price,
				total_fee = total_fee,	
				create_time=create_time,      
				notes=notes)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))


@csrf_exempt
def modify_order(request):
	id=request.POST.get('id', None)
	productID = request.POST.get('productID', None)	
	customer = request.POST.get('customer', None)
	contacts = request.POST.get('contacts', None)
	contacts_phone = request.POST.get('contacts_phone', None)
	fax = request.POST.get('fax', None)		
	qq = request.POST.get('qq', None)
	create_time = request.POST.get('create_time', None)
	product_name = request.POST.get('product_name', None)
	amount = request.POST.get('amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	edition_fee = request.POST.get('edition_fee', None)
	total_fee = request.POST.get('total_fee', None)
	deadline = request.POST.get('deadline', None)
	feilin = request.POST.get('feilin', None)
	material = request.POST.get('material', None)
	size = request.POST.get('size', None)
	surface = request.POST.get('surface', None)
	wl_material = request.POST.get('wl_material', None)
	wl_kind = request.POST.get('wl_kind', None)
	mould = request.POST.get('mould', None)
	notes = request.POST.get('notes', None)	
	delivery_address = request.POST.get('delivery_address', None)
	call = request.POST.get('call', None)
	productID2 = request.POST.get('productID2', None)
	
	try:
		Order.objects.filter(id=id).update(productID=productID,
				customer = customer,
				contacts=contacts,
				contacts_phone=contacts_phone,
				fax = fax,
				qq=qq,
				create_time=create_time,
				product_name=product_name,				
				amount = amount,
				price=price,
				fee = fee,
				edition_fee=edition_fee,
				total_fee = total_fee,
				deadline=deadline,
				feilin = feilin,
				material = material,
				size = size,
				surface=surface,
				wl_material=wl_material,
				wl_kind=wl_kind,
				mould=mould,      
				notes=notes,
				delivery_address=delivery_address,
				call=call,
				productID2=productID2)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	
	return HttpResponse(json.dumps(1))

#删除报价单
@csrf_exempt
def delete_order(request):
	id = request.POST.get('id', None)
	try:
		Order.objects.filter(orderID=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))
#api
@csrf_exempt
def get_orderID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Order.objects.filter(product_name=product_name)
	if r:
		quotationID=r[0].id
		return HttpResponse(quotationID)
	else:
		return HttpResponse(0)		
#api
@csrf_exempt
def get_orderID_by_customer(request):
	customer = request.POST.get('customer', None)
	r=Order.objects.filter(customer=customer)
	if r:
		quotationID=r[0].id
		return HttpResponse(quotationID)
	else:
		return HttpResponse(0)	

#################################################################################
#送货单
#订单单列表
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
		a[i]=b
		i=i+1
	return a

def delivery_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	quotation=False
	order=False
	delivery=True
	process=False
	cost=False
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Delivery.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Delivery.objects.all().order_by('-id')
				a=get_delivery_list(records)
			else:
				records=Delivery.objects.all().order_by('-id')[0:10]
				a=get_delivery_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Delivery.objects.all().order_by('-id')[last:]
				a=get_delivery_list(records)
			else:
				first=int(num)*10
				records=Delivery.objects.all().order_by('-id')[first:int(first+10)]
				a=get_delivery_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("sales_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,"quotation":quotation,'order':order,'delivery':delivery,'process':process,'cost':cost,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})


def delivery_new(request,choice):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Delivery.objects.all().order_by('-id')
		if records:
			deliveryID=int(records[0].deliveryID)+1
		else:
			deliveryID=1
		if(int(choice)==1):
			return render_to_response("sales_delivery_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"choice":json.dumps(choice),'deliveryID':deliveryID})
		elif(int(choice)==2):
			return render_to_response("sales_delivery_new_2.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"choice":json.dumps(choice),'deliveryID':deliveryID})
		elif(int(choice)==3):
			return render_to_response("sales_delivery_new_3.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"choice":json.dumps(choice),'deliveryID':deliveryID})


#报价单单页
def delivery(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		delivery_show=True
		delivery_modify=False
		print delivery_modify
		choice=int(Delivery.objects.filter(deliveryID=id)[0].choice)
		if(choice==1):
			records=Delivery.objects.filter(deliveryID=id)
			a={}
			i=0
			for r in records:
				b={}
				b[0]=r.deliveryID
				b[1]=r.delivery_name
				b[2]=r.delivery_time
				b[3]=r.productID
				b[4]=r.product_name
				b[5]=r.order_amount
				b[6]=r.delivery_amount
				b[7]=r.price
				b[8]=r.fee
				b[9]=r.notes
				b[10]=r.delivery_address
				b[11]=r.total_fee
				b[12]=r.receive_man
				b[13]=r.delivery_man
				b[14]=int(i+1)
				a[i]=b
				i=i+1
			return render_to_response("sales_delivery.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'delivery_show':json.dumps(delivery_show),'delivery_modify':json.dumps(delivery_modify),'length':json.dumps(i)})
		elif(choice==2):
			records=Delivery.objects.filter(deliveryID=id)
			a={}
			i=0
			for r in records:
				b={}
				b[0]=r.deliveryID
				b[1]=r.delivery_name
				b[2]=r.delivery_time
				b[3]=r.productID
				b[4]=r.product_name
				b[5]=r.order_amount
				b[6]=r.delivery_amount
				b[7]=r.price
				b[8]=r.fee
				b[9]=r.notes
				b[10]=r.delivery_address
				b[11]=r.total_fee
				b[12]=r.receive_man
				b[13]=r.delivery_man
				b[14]=int(i+1)
				b[15]=r.send_name
				b[16]=r.purchase_man
				b[17]=r.product_number
				b[18]=r.perbox
				b[19]=r.box
				a[i]=b
				i=i+1
			return render_to_response("sales_delivery_2.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'delivery_show':json.dumps(delivery_show),'delivery_modify':json.dumps(delivery_modify),'length':json.dumps(i)})
		elif(choice==3):
			records=Delivery.objects.filter(deliveryID=id)
			a={}
			i=0
			for r in records:
				b={}
				b[0]=r.deliveryID
				b[1]=r.delivery_name
				b[2]=r.delivery_time
				b[3]=r.productID
				b[4]=r.product_name
				b[5]=r.order_amount
				b[6]=r.delivery_amount
				b[7]=r.price
				b[8]=r.fee
				b[9]=r.notes
				b[10]=r.delivery_address
				b[11]=r.total_fee
				b[12]=r.receive_man
				b[13]=r.delivery_man
				b[14]=int(i+1)
				b[15]=r.send_phone
				b[16]=r.send_fax
				b[17]=r.receive_phone
				b[18]=r.receive_fax
				b[19]=r.box
				b[20]=r.inner_amount
				b[21]=r.outer_amount
				b[22]=r.purchase_man
				b[23]=r.send_name
				b[24]=r.huoID
				b[25]=r.total_notes
				a[i]=b
				i=i+1
			return render_to_response("sales_delivery_3.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'delivery_show':json.dumps(delivery_show),'delivery_modify':json.dumps(delivery_modify),'length':json.dumps(i)})
				
#api
#报价单单页
def delivery_modify(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		delivery_show=False
		delivery_modify=True
		choice=int(Delivery.objects.filter(deliveryID=id)[0].choice)
		if(choice==1):
			records=Delivery.objects.filter(deliveryID=id)
			a={}
			i=0
			for r in records:
				b={}
				b[0]=r.deliveryID
				b[1]=r.delivery_name
				b[2]=r.delivery_time
				b[3]=r.productID
				b[4]=r.product_name
				b[5]=r.order_amount
				b[6]=r.delivery_amount
				b[7]=r.price
				b[8]=r.fee
				b[9]=r.notes
				b[10]=r.delivery_address
				b[11]=r.total_fee
				b[12]=r.receive_man
				b[13]=r.delivery_man
				b[14]=int(i+1)
				a[i]=b
				i=i+1
			return render_to_response("sales_delivery.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'delivery_show':json.dumps(delivery_show),'delivery_modify':json.dumps(delivery_modify),'length':json.dumps(i)})
		elif(choice==2):
			records=Delivery.objects.filter(deliveryID=id)
			a={}
			i=0
			for r in records:
				b={}
				b[0]=r.deliveryID
				b[1]=r.delivery_name
				b[2]=r.delivery_time
				b[3]=r.productID
				b[4]=r.product_name
				b[5]=r.order_amount
				b[6]=r.delivery_amount
				b[7]=r.price
				b[8]=r.fee
				b[9]=r.notes
				b[10]=r.delivery_address
				b[11]=r.total_fee
				b[12]=r.receive_man
				b[13]=r.delivery_man
				b[14]=int(i+1)
				b[15]=r.send_name
				b[16]=r.purchase_man
				b[17]=r.product_number
				b[18]=r.perbox
				b[19]=r.box
				a[i]=b
				i=i+1
			return render_to_response("sales_delivery_2.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'delivery_show':json.dumps(delivery_show),'delivery_modify':json.dumps(delivery_modify),'length':json.dumps(i)})
		elif(choice==3):
			records=Delivery.objects.filter(deliveryID=id)
			a={}
			i=0
			for r in records:
				b={}
				b[0]=r.deliveryID
				b[1]=r.delivery_name
				b[2]=r.delivery_time
				b[3]=r.productID
				b[4]=r.product_name
				b[5]=r.order_amount
				b[6]=r.delivery_amount
				b[7]=r.price
				b[8]=r.fee
				b[9]=r.notes
				b[10]=r.delivery_address
				b[11]=r.total_fee
				b[12]=r.receive_man
				b[13]=r.delivery_man
				b[14]=int(i+1)
				b[15]=r.send_phone
				b[16]=r.send_fax
				b[17]=r.receive_phone
				b[18]=r.receive_fax
				b[19]=r.box
				b[20]=r.inner_amount
				b[21]=r.outer_amount
				b[22]=r.purchase_man
				b[23]=r.send_name
				b[24]=r.huoID
				b[25]=r.total_notes	
				a[i]=b
				i=i+1
			return render_to_response("sales_delivery_3.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'delivery_show':json.dumps(delivery_show),'delivery_modify':json.dumps(delivery_modify),'length':json.dumps(i)})
	
	
	#api

@csrf_exempt
def fill_delivery(request):
	deliveryID = request.POST.get('deliveryID', None)
	choice = request.POST.get('choice', None)		
	delivery_name = request.POST.get('delivery_name', None)
	delivery_time = request.POST.get('delivery_time', None)
	receive_man = request.POST.get('receive_man', None)
	delivery_man = request.POST.get('delivery_name', None)
	delivery_address = request.POST.get('delivery_address', None)
	total_fee = request.POST.get('total_fee', None)
	productID = request.POST.get('productID', None)		
	product_name = request.POST.get('product_name', None)
	order_amount = request.POST.get('order_amount', None)
	delivery_amount = request.POST.get('delivery_amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	notes = request.POST.get('notes', None)

	try:
		q = Delivery(deliveryID = deliveryID,
                choice = choice,
                delivery_name = delivery_name,
                delivery_time=delivery_time,
                receive_man=receive_man,
                delivery_man=delivery_man,
                delivery_address=delivery_address,
                total_fee = total_fee,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                fee=fee,
                notes=notes)
		q.save()
	except Exception, e:
		return comutils.baseresponse("system error", 500)
	try:
		q = Finance(delivery_time=delivery_time,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                total_fee=fee,
                notes=notes)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	try:
		total_amount=Storage.objects.filter(productID=productID)[0].amount
		now_amount=int(total_amount)-int(delivery_amount)
		print delivery_time
		Storage.objects.filter(productID=productID).update(out_time=delivery_time,amount=now_amount)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))


@csrf_exempt
def modify_delivery(request):
	deliveryID = request.POST.get('deliveryID', None)
	choice = request.POST.get('choice', None)		
	delivery_name = request.POST.get('delivery_name', None)
	delivery_time = request.POST.get('delivery_time', None)
	receive_man = request.POST.get('receive_man', None)
	delivery_man = request.POST.get('delivery_name', None)
	delivery_address = request.POST.get('delivery_address', None)
	total_fee = request.POST.get('total_fee', None)
	productID = request.POST.get('productID', None)		
	product_name = request.POST.get('product_name', None)
	order_amount = request.POST.get('order_amount', None)
	delivery_amount = request.POST.get('delivery_amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	notes = request.POST.get('notes', None)

	try:
		Delivery.objects.filter(productID = productID).update(delivery_name = delivery_name,
                delivery_time=delivery_time,
                receive_man=receive_man,
                delivery_man=delivery_man,
                delivery_address=delivery_address,
                total_fee = total_fee,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                fee=fee,
                notes=notes)
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))

#删除报价单
@csrf_exempt
def delete_delivery(request):
	deliveryID = request.POST.get('deliveryID', None)
	try:
		Delivery.objects.filter(deliveryID=deliveryID).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))
#api

@csrf_exempt
def get_deliveryID_by_deliveryID(request):
	deliveryID = request.POST.get('deliveryID', None)
	r=Delivery.objects.filter(deliveryID=deliveryID)
	if r:
		return HttpResponse(deliveryID)
	else:
		return HttpResponse(0)

@csrf_exempt
def get_deliveryID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Delivery.objects.filter(product_name=product_name)
	if r:
		deliveryID=r[0].deliveryID
		return HttpResponse(deliveryID)
	else:
		return HttpResponse(0)
#api
@csrf_exempt
def get_details_from_order(request):
	productID = request.POST.get('productID', None)
	records=Order.objects.filter(productID=productID)
	if records:
		r=records[0]
		a={}
		a[0]=r.product_name
		a[1]=r.amount
		a[2]=r.price
		a[3]=r.fee
		a[4]=r.notes
		return HttpResponse(json.dumps(a))
	else:
		return HttpResponse(json.dumps(0))
	#api

#######特殊情况2

@csrf_exempt
def fill_delivery_2(request):
	deliveryID = request.POST.get('deliveryID', None)
	choice = request.POST.get('choice', None)		
	delivery_name = request.POST.get('delivery_name', None)
	delivery_time = request.POST.get('delivery_time', None)
	receive_man = request.POST.get('receive_man', None)
	delivery_man = request.POST.get('delivery_name', None)
	delivery_address = request.POST.get('delivery_address', None)
	total_fee = request.POST.get('total_fee', None)
	productID = request.POST.get('productID', None)		
	product_name = request.POST.get('product_name', None)
	order_amount = request.POST.get('order_amount', None)
	delivery_amount = request.POST.get('delivery_amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	notes = request.POST.get('notes', None)
	send_name = request.POST.get('send_name', None)
	purchase_man = request.POST.get('purchase_man', None)
	product_number = request.POST.get('product_number', None)
	perbox = request.POST.get('perbox', None)
	box = request.POST.get('box', None)

	try:
		q = Delivery(deliveryID = deliveryID,
                choice = choice,
                delivery_name = delivery_name,
                delivery_time=delivery_time,
                receive_man=receive_man,
                delivery_man=delivery_man,
                delivery_address=delivery_address,
                total_fee = total_fee,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                fee=fee,
                notes=notes,
                product_number=product_number,
                perbox=perbox,
                box=box,
                purchase_man=purchase_man,
                send_name=send_name)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	try:
		q = Finance(delivery_time=delivery_time,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                total_fee=fee,
                notes=notes)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	try:
		total_amount=Storage.objects.filter(productID=productID)[0].amount
		now_amount=int(total_amount)-int(delivery_amount)
		Storage.objects.filter(productID=productID).update(out_time=delivery_time,amount=now_amount)
	except Exception, e:
		return comutils.baseresponse("库存中没有该产品", 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def modify_delivery_2(request):
	deliveryID = request.POST.get('deliveryID', None)
	choice = request.POST.get('choice', None)		
	delivery_name = request.POST.get('delivery_name', None)
	delivery_time = request.POST.get('delivery_time', None)
	receive_man = request.POST.get('receive_man', None)
	delivery_man = request.POST.get('delivery_name', None)
	delivery_address = request.POST.get('delivery_address', None)
	total_fee = request.POST.get('total_fee', None)
	productID = request.POST.get('productID', None)		
	product_name = request.POST.get('product_name', None)
	order_amount = request.POST.get('order_amount', None)
	delivery_amount = request.POST.get('delivery_amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	notes = request.POST.get('notes', None)
	send_name = request.POST.get('send_name', None)
	purchase_man = request.POST.get('purchase_man', None)
	product_number = request.POST.get('product_number', None)
	perbox = request.POST.get('perbox', None)
	box = request.POST.get('box', None)

	try:
		Delivery.objects.filter(productID = productID).update(delivery_name = delivery_name,
                delivery_time=delivery_time,
                receive_man=receive_man,
                delivery_man=delivery_man,
                delivery_address=delivery_address,
                total_fee = total_fee,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                fee=fee,
                notes=notes,
                product_number=product_number,
                perbox=perbox,
                box=box,
                purchase_man=purchase_man,
                send_name=send_name)
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))

@csrf_exempt
def fill_delivery_3(request):
	deliveryID = request.POST.get('deliveryID', None)
	choice = request.POST.get('choice', None)		
	delivery_name = request.POST.get('delivery_name', None)
	delivery_time = request.POST.get('delivery_time', None)
	receive_man = request.POST.get('receive_man', None)
	delivery_man = request.POST.get('delivery_name', None)
	delivery_address = request.POST.get('delivery_address', None)
	total_fee = request.POST.get('total_fee', None)
	productID = request.POST.get('productID', None)		
	product_name = request.POST.get('product_name', None)
	order_amount = request.POST.get('order_amount', None)
	delivery_amount = request.POST.get('delivery_amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	notes = request.POST.get('notes', None)
	send_phone = request.POST.get('send_phone', None)
	send_fax = request.POST.get('send_fax', None)
	receive_phone = request.POST.get('receive_phone', None)
	receive_fax = request.POST.get('receive_fax', None)
	total_notes = request.POST.get('total_notes', None)
	box = request.POST.get('box', None)
	inner_amount = request.POST.get('inner_amount', None)
	outer_amount = request.POST.get('outer_amount', None)
	purchase_man = request.POST.get('purchase_man', None)
	send_name = request.POST.get('send_name', None)
	huoID = request.POST.get('huoID', None)

	try:
		q = Delivery(deliveryID = deliveryID,
                choice = choice,
                delivery_name = delivery_name,
                delivery_time=delivery_time,
                receive_man=receive_man,
                delivery_man=delivery_man,
                delivery_address=delivery_address,
                total_fee = total_fee,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                fee=fee,
                notes=notes,
                send_phone=send_phone,
                send_fax=send_fax,
                receive_phone=receive_phone,
                receive_fax=receive_fax,
                box=box,
                inner_amount=inner_amount,
                outer_amount=outer_amount,
                purchase_man=purchase_man,
                total_notes=total_notes,
                send_name=send_name,
                huoID=huoID)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	try:
		q = Finance(delivery_time=delivery_time,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                total_fee=fee,
                notes=notes)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	try:
		total_amount=Storage.objects.filter(productID=productID)[0].amount
		now_amount=int(total_amount)-int(delivery_amount)
		Storage.objects.filter(productID=productID).update(out_time=delivery_time,amount=now_amount)
	except Exception, e:
		return comutils.baseresponse("库存中没有该产品", 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def modify_delivery_3(request):
	deliveryID = request.POST.get('deliveryID', None)
	choice = request.POST.get('choice', None)		
	delivery_name = request.POST.get('delivery_name', None)
	delivery_time = request.POST.get('delivery_time', None)
	receive_man = request.POST.get('receive_man', None)
	delivery_man = request.POST.get('delivery_name', None)
	delivery_address = request.POST.get('delivery_address', None)
	total_fee = request.POST.get('total_fee', None)
	productID = request.POST.get('productID', None)		
	product_name = request.POST.get('product_name', None)
	order_amount = request.POST.get('order_amount', None)
	delivery_amount = request.POST.get('delivery_amount', None)
	price = request.POST.get('price', None)
	fee = request.POST.get('fee', None)
	notes = request.POST.get('notes', None)
	send_phone = request.POST.get('send_phone', None)
	send_fax = request.POST.get('send_fax', None)
	receive_phone = request.POST.get('receive_phone', None)
	receive_fax = request.POST.get('receive_fax', None)
	total_notes = request.POST.get('total_notes', None)
	box = request.POST.get('box', None)
	inner_amount = request.POST.get('inner_amount', None)
	outer_amount = request.POST.get('outer_amount', None)
	purchase_man = request.POST.get('purchase_man', None)
	send_name = request.POST.get('send_name', None)
	huoID = request.POST.get('huoID', None)

	try:
		Delivery.objects.filter(productID = productID).update(delivery_name = delivery_name,
                delivery_time=delivery_time,
                receive_man=receive_man,
                delivery_man=delivery_man,
                delivery_address=delivery_address,
                total_fee = total_fee,
                productID = productID,
                product_name = product_name,
                order_amount=order_amount,
                delivery_amount=delivery_amount,
                price=price,
                fee=fee,
                notes=notes,
                send_phone=send_phone,
                send_fax=send_fax,
                receive_phone=receive_phone,
                receive_fax=receive_fax,
                box=box,
                inner_amount=inner_amount,
                outer_amount=outer_amount,
                purchase_man=purchase_man,
                total_notes=total_notes,
                send_name=send_name,
                huoID=huoID)
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))


################################################################################
#施工单
#报价单列表
def get_process_list(records):
	a={}
	i=0
	for r in records:
		b={}
		b[1]=r.customer
		b[2]=r.product_name
		b[3]=r.create_time
		b[4]=r.finished
		b[0]=r.productID
		a[i]=b
		i=i+1
	return a

def process_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	quotation=False
	order=False
	delivery=False
	process=True
	cost=False
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Process.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Process.objects.all().order_by('-id')
				a=get_process_list(records)
			else:
				records=Process.objects.all().order_by('-id')[0:10]
				a=get_process_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Process.objects.all().order_by('-id')[last:]
				a=get_process_list(records)
			else:
				first=int(num)*10
				records=Process.objects.all().order_by('-id')[first:int(first+10)]
				a=get_process_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("sales_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,"quotation":quotation,'order':order,'delivery':delivery,'process':process,'cost':cost,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})


def process_new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Process.objects.all().order_by('-id')
		if records:
			productID=int(records[0].productID)+1
		else:
			productID=1
		return render_to_response("sales_process_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'productID':productID})

#api

@csrf_exempt
def fill_process(request):
	productID = request.POST.get('productID', None)	
	customer = request.POST.get('customer', None)
	create_time = request.POST.get('create_time', None)
	deadline = request.POST.get('deadline', None)
	alerttime = request.POST.get('alerttime', None)
	product_name = request.POST.get('product_name', None)
	number_1 = request.POST.get('number_1', None)
	number_2 = request.POST.get('number_2', None)
	amount = request.POST.get('amount', None)
	pinban = request.POST.get('pinban', None)
	yinshu = request.POST.get('yinshu', None)
	yinsha = request.POST.get('yinsha', None)
	jiayinshu = request.POST.get('jiayinshu', None)
	zhenjiao = request.POST.get('zhenjiao', None)
	total_yinshu = request.POST.get('total_yinshu', None)
	yaheng = request.POST.get('yaheng', None)
	lingyin = request.POST.get('lingyin', None)
	surface = request.POST.get('surface', None)
	process = request.POST.get('process', None)
	notes = request.POST.get('notes', None)
	material = request.POST.get('material', None)	
	daliao = request.POST.get('daliao', None)
	size = request.POST.get('size', None)
	kaiyin = request.POST.get('kaiyin', None)
	kaishu = request.POST.get('kaishu', None)
	fudai = request.POST.get('fudai', None)
	quality = request.POST.get('quality', None)
	wl_biaoliao = request.POST.get('wl_biaoliao', None)
	wl_size = request.POST.get('wl_size', None)
	wl_size2 = request.POST.get('wl_size2', None)
	wl_feizhi = request.POST.get('wl_feizhi', None)
	wl_thin = request.POST.get('wl_thin', None)
	wl_waleng = request.POST.get('wl_waleng', None)
	yinsha2 = request.POST.get('yinsha2', None)
	total_yinshu_1 = request.POST.get('total_yinshu_1', None)
	total_yinshu_2 = request.POST.get('total_yinshu_2', None)
	try:
		q = Process(productID=productID,
				customer = customer,
				create_time=create_time,
				deadline=deadline,
				alerttime=alerttime,
				product_name=product_name,	
				number_1=number_1,
				number_2=number_2,			
				amount = amount,
				pinban=pinban,
				yinshu = yinshu,
				yinsha=yinsha,
				jiayinshu = jiayinshu,
				zhenjiao=zhenjiao,
				total_yinshu = total_yinshu,
				yaheng = yaheng,
				lingyin = lingyin,
				surface=surface,
				process=process,
				notes=notes,
				material=material,
				daliao=daliao,      
				size=size,
				kaishu=kaishu,
				kaiyin=kaiyin,
				fudai=fudai,
				quality=quality,
				wl_size=wl_size,
				wl_size2=wl_size2,
				wl_thin=wl_thin,
				wl_feizhi=wl_feizhi,
				wl_biaoliao=wl_biaoliao,
				wl_waleng=wl_waleng,
				yinsha2=yinsha2,
				total_yinshu_2=total_yinshu_2,
				total_yinshu_1=total_yinshu_1)
		q.save()
		p = Storage(productID=productID,
				customer = customer,
				product_name=product_name,	
				size=size,					
				amount = amount,
				in_time = create_time,
				notes=notes)
		p.save()
	except Exception, e:
		return comutils.baseresponse("system error", 500)
	try:
		q = Tracking(productID=productID,
				product_name=product_name,
				customer = customer,
				create_time=create_time,
				deadline=deadline,
				notes=notes)
		q.save()
	except Exception, e:
		return comutils.baseresponse("自动生成产品追踪单错误", 500)
	

	return HttpResponse(json.dumps(1))

#报价单单页
def process(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		process_show=True
		process_modify=False
		r=Process.objects.filter(productID=id)[0]
		b={}
		b[0]=r.productID
		b[1]=r.customer
		b[2]=r.create_time
		b[3]=r.deadline
		b[4]=r.alerttime
		b[5]=r.product_name
		b[6]=r.number_1
		b[7]=r.number_2
		b[8]=r.amount
		b[9]=r.pinban
		b[10]=r.yinshu
		b[11]=r.yinsha
		b[12]=r.jiayinshu
		b[13]=r.zhenjiao
		b[14]=r.total_yinshu
		b[15]=r.yaheng
		b[16]=r.lingyin
		b[17]=r.surface
		b[18]=r.process
		b[19]=r.notes
		b[20]=r.material
		b[21]=r.daliao
		b[22]=r.size
		b[23]=r.kaishu
		b[24]=r.kaiyin
		b[25]=r.fudai
		b[26]=r.quality
		b[27]=r.wl_size
		b[28]=r.wl_size2
		b[29]=r.wl_thin
		b[30]=r.wl_feizhi
		b[31]=r.wl_waleng
		b[32]=r.wl_biaoliao
		b[33]=r.yinsha2
		b[34]=r.total_yinshu_1
		b[35]=r.total_yinshu_2
		return render_to_response("sales_process.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b,'process_show':json.dumps(process_show),'process_modify':json.dumps(process_modify)})
#api
#报价单单页
def process_modify(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		process_show=False
		process_modify=True
		r=Process.objects.filter(productID=id)[0]
		b={}
		b[0]=r.productID
		b[1]=r.customer
		b[2]=r.create_time
		b[3]=r.deadline
		b[4]=r.alerttime
		b[5]=r.product_name
		b[6]=r.number_1
		b[7]=r.number_2
		b[8]=r.amount
		b[9]=r.pinban
		b[10]=r.yinshu
		b[11]=r.yinsha
		b[12]=r.jiayinshu
		b[13]=r.zhenjiao
		b[14]=r.total_yinshu
		b[15]=r.yaheng
		b[16]=r.lingyin
		b[17]=r.surface
		b[18]=r.process
		b[19]=r.notes
		b[20]=r.material
		b[21]=r.daliao
		b[22]=r.size
		b[23]=r.kaishu
		b[24]=r.kaiyin
		b[25]=r.fudai
		b[26]=r.quality
		b[27]=r.wl_size
		b[28]=r.wl_size2
		b[29]=r.wl_thin
		b[30]=r.wl_feizhi
		b[31]=r.wl_waleng
		b[32]=r.wl_biaoliao
		b[33]=r.yinsha2
		b[34]=r.total_yinshu_1
		b[35]=r.total_yinshu_2
		return render_to_response("sales_process.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b,'process_show':json.dumps(process_show),'process_modify':json.dumps(process_modify)})
#api
#api

@csrf_exempt
def modify_process(request):
	productID = request.POST.get('productID', None)	
	customer = request.POST.get('customer', None)
	create_time = request.POST.get('create_time', None)
	deadline = request.POST.get('deadline', None)
	alerttime = request.POST.get('alerttime', None)
	product_name = request.POST.get('product_name', None)
	number_1 = request.POST.get('number_1', None)
	number_2 = request.POST.get('number_2', None)
	amount = request.POST.get('amount', None)
	pinban = request.POST.get('pinban', None)
	yinshu = request.POST.get('yinshu', None)
	yinsha = request.POST.get('yinsha', None)
	jiayinshu = request.POST.get('jiayinshu', None)
	zhenjiao = request.POST.get('zhenjiao', None)
	total_yinshu = request.POST.get('total_yinshu', None)
	yaheng = request.POST.get('yaheng', None)
	lingyin = request.POST.get('lingyin', None)
	surface = request.POST.get('surface', None)
	process = request.POST.get('process', None)
	notes = request.POST.get('notes', None)
	material = request.POST.get('material', None)	
	daliao = request.POST.get('daliao', None)
	size = request.POST.get('size', None)
	kaiyin = request.POST.get('kaiyin', None)
	kaishu = request.POST.get('kaishu', None)
	fudai = request.POST.get('fudai', None)
	quality = request.POST.get('quality', None)
	wl_biaoliao = request.POST.get('wl_biaoliao', None)
	wl_size = request.POST.get('wl_size', None)
	wl_size2 = request.POST.get('wl_size2', None)
	wl_feizhi = request.POST.get('wl_feizhi', None)
	wl_thin = request.POST.get('wl_thin', None)
	wl_waleng = request.POST.get('wl_waleng', None)
	yinsha2 = request.POST.get('yinsha2', None)
	total_yinshu_1 = request.POST.get('total_yinshu_1', None)
	total_yinshu_2 = request.POST.get('total_yinshu_2', None)

	try:
		Process.objects.filter(productID=productID).update(productID=productID,
				customer = customer,
				create_time=create_time,
				deadline=deadline,
				alerttime=alerttime,
				product_name=product_name,	
				number_1=number_1,
				number_2=number_2,			
				amount = amount,
				pinban=pinban,
				yinshu = yinshu,
				yinsha=yinsha,
				jiayinshu = jiayinshu,
				zhenjiao=zhenjiao,
				total_yinshu = total_yinshu,
				yaheng = yaheng,
				lingyin = lingyin,
				surface=surface,
				process=process,
				notes=notes,
				material=material,
				daliao=daliao,      
				size=size,
				kaishu=kaishu,
				kaiyin=kaiyin,
				fudai=fudai,
				quality=quality,
				wl_size=wl_size,
				wl_size2=wl_size2,
				wl_thin=wl_thin,
				wl_feizhi=wl_feizhi,
				wl_biaoliao=wl_biaoliao,
				wl_waleng=wl_waleng,
				yinsha2=yinsha2,
				total_yinshu_2=total_yinshu_2,
				total_yinshu_1=total_yinshu_1)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	
	return HttpResponse(json.dumps(1))

#删除报价单
@csrf_exempt
def delete_process(request):
	id = request.POST.get('id', None)
	try:
		Process.objects.filter(productID=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))
#api
@csrf_exempt
def get_processID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Process.objects.filter(product_name=product_name)
	if r:	
		id=r[0].productID
		return HttpResponse(id)
	else:
		return HttpResponse(0)
#api
@csrf_exempt
def get_processID_by_customer(request):
	customer = request.POST.get('customer', None)
	r=Process.objects.filter(customer=customer)
	if r:	
		id=r[0].productID
		return HttpResponse(id)
	else:
		return HttpResponse(0)


################################################################################

#成本单列表
#报价单列表
def get_cost_list(records):
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.productID
		b[1]=r.customer
		b[2]=r.product_name
		b[3]=r.total_fee
		b[4]=r.id
		a[i]=b
		i=i+1
	return a

def cost_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	quotation=False
	order=False
	delivery=False
	process=False
	cost=True
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Cost.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Cost.objects.all().order_by('-id')
				a=get_cost_list(records)
			else:
				records=Cost.objects.all().order_by('-id')[0:10]
				a=get_cost_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Cost.objects.all().order_by('-id')[last:]
				a=get_cost_list(records)
			else:
				first=int(num)*10
				records=Process.objects.all().order_by('-id')[first:int(first+10)]
				a=get_process_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("sales_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,"quotation":quotation,'order':order,'delivery':delivery,'process':process,'cost':cost,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})


def cost_new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		return render_to_response("sales_cost_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name})



@csrf_exempt
def get_details_from_process(request):
	productID = request.POST.get('productID', None)
	r=Process.objects.filter(productID=productID)[0]
	b={}
	b[0]=r.productID
	b[1]=r.customer
	b[2]=r.product_name
	b[3]=r.create_time
	b[4]=r.surface
	b[5]=r.material
	b[6]=r.wl_feizhi
	b[7]=r.wl_waleng
	b[8]=r.daliao
	b[9]=r.size
	return HttpResponse(json.dumps(b))


@csrf_exempt
def fill_cost(request):
	productID = request.POST.get('productID', None)
	customer = request.POST.get('customer', None)		
	product_name = request.POST.get('product_name', None)
	create_time = request.POST.get('create_time', None)
	surface= request.POST.get('surface', None)
	material = request.POST.get('material', None)
	wl_waleng = request.POST.get('wl_waleng', None)
	wl_feizhi = request.POST.get('wl_feizhi', None)		
	surface_price = request.POST.get('surface_price', None)
	material_price = request.POST.get('material_price', None)
	wl_feizhi_price= request.POST.get('wl_feizhi_price', None)
	wl_waleng_price = request.POST.get('wl_waleng_price', None)
	daliao = request.POST.get('daliao', None)	
	size = request.POST.get('size', None)
	worker_fee= request.POST.get('worker_fee', None)
	other_fee = request.POST.get('other_fee', None)
	notes = request.POST.get('notes', None)
	total_fee = request.POST.get('total_fee', None)
	try:
		q = Cost(productID = productID,
                customer = customer,
                product_name = product_name,
                create_time=create_time,
                surface=surface,
                material=material,
                wl_waleng = wl_waleng,
                wl_feizhi = wl_feizhi,
                surface_price=surface_price,
                material_price=material_price,
                wl_feizhi_price=wl_feizhi_price,
                wl_waleng_price = wl_waleng_price,
                daliao = daliao,
                size=size,
                worker_fee=worker_fee,
                other_fee=other_fee,
                notes = notes,
                total_fee = total_fee)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))

def cost(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		cost_show=True
		cost_modify=False
		r=Cost.objects.filter(productID=id)[0]
		b={}
		b[0]=r.productID
		b[1]=r.customer
		b[2]=r.product_name
		b[3]=r.create_time
		b[4]=r.surface
		b[5]=r.surface_price
		b[6]=r.material
		b[7]=r.material_price
		b[8]=r.wl_feizhi
		b[9]=r.wl_feizhi_price
		b[10]=r.wl_waleng
		b[11]=r.wl_waleng_price
		b[12]=r.daliao
		b[13]=r.size
		b[14]=r.worker_fee
		b[15]=r.other_fee
		b[16]=r.notes
		b[17]=r.total_fee
		return render_to_response("sales_cost.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b,'cost_show':json.dumps(cost_show),'cost_modify':json.dumps(cost_modify)})
#api

def cost_modify(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		cost_show=False
		cost_modify=True
		r=Cost.objects.filter(productID=id)[0]
		b={}
		b[0]=r.productID
		b[1]=r.customer
		b[2]=r.product_name
		b[3]=r.create_time
		b[4]=r.surface
		b[5]=r.surface_price
		b[6]=r.material
		b[7]=r.material_price
		b[8]=r.wl_feizhi
		b[9]=r.wl_feizhi_price
		b[10]=r.wl_waleng
		b[11]=r.wl_waleng_price
		b[12]=r.daliao
		b[13]=r.size
		b[14]=r.worker_fee
		b[15]=r.other_fee
		b[16]=r.notes
		b[17]=r.total_fee
		return render_to_response("sales_cost.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b,'cost_show':json.dumps(cost_show),'cost_modify':json.dumps(cost_modify)})
#api

@csrf_exempt
def modify_cost(request):
	productID = request.POST.get('productID', None)
	customer = request.POST.get('customer', None)		
	product_name = request.POST.get('product_name', None)
	create_time = request.POST.get('create_time', None)
	surface= request.POST.get('surface', None)
	material = request.POST.get('material', None)
	wl_waleng = request.POST.get('wl_waleng', None)
	wl_feizhi = request.POST.get('wl_feizhi', None)		
	surface_price = request.POST.get('surface_price', None)
	material_price = request.POST.get('material_price', None)
	wl_feizhi_price= request.POST.get('wl_feizhi_price', None)
	wl_waleng_price = request.POST.get('wl_waleng_price', None)
	daliao = request.POST.get('daliao', None)	
	size = request.POST.get('size', None)
	worker_fee= request.POST.get('worker_fee', None)
	other_fee = request.POST.get('other_fee', None)
	notes = request.POST.get('notes', None)
	total_fee = request.POST.get('total_fee', None)
	try:
		Cost.objects.filter(productID=productID).update(productID = productID,
                customer = customer,
                product_name = product_name,
                create_time=create_time,
                surface=surface,
                material=material,
                wl_waleng = wl_waleng,
                wl_feizhi = wl_feizhi,
                surface_price=surface_price,
                material_price=material_price,
                wl_feizhi_price=wl_feizhi_price,
                wl_waleng_price = wl_waleng_price,
                daliao = daliao,
                size=size,
                worker_fee=worker_fee,
                other_fee=other_fee,
                notes = notes,
                total_fee = total_fee)
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))
#删除报价单
@csrf_exempt
def delete_cost(request):
	id = request.POST.get('id', None)
	try:
		Cost.objects.filter(productID=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))
#api
@csrf_exempt
def get_costID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Cost.objects.filter(product_name=product_name)
	if r:
		id=r[0].productID
		return HttpResponse(id)
	else:
		return HttpResponse(0)
#api
@csrf_exempt
def get_costID_by_customer(request):
	customer = request.POST.get('customer', None)
	r=Cost.objects.filter(customer=customer)
	if r:
		id=r[0].productID
		return HttpResponse(id)
	else:
		return HttpResponse(0)

	