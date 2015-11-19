#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from storage.models import Storage,Storage_in,Storage_out,Storage_material

def storage(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Storage.objects.all()
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.customer
			b[1]=r.product_name
			b[2]=r.size
			b[3]=r.amount
			b[4]=r.in_time
			b[5]=r.out_time
			b[6]=r.notes
			b[7]=r.productID
			b[8]=i
			a[i]=b
			i=i+1
		return render_to_response("storage_storage.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})

#################################################################
def storage_in(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Storage_in.objects.all()
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.storage_in_id
			b[1]=r.material_name
			b[2]=r.create_time
			b[3]=r.seller
			b[4]=r.amount
			b[5]=r.total_fee	
			a[i]=b
			i=i+1
		return render_to_response("storage_storage_in.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})

def storage_in_show(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Storage_in.objects.filter(storage_in_id=id)
		a={}
		i=0
		for r in records:
			b={}
			b[0]=int(i+1)
			b[1]=r.material_name
			b[2]=r.size
			b[3]=r.seller
			b[4]=r.amount
			b[5]=r.price		
			b[6]=r.total_fee
			b[7]=r.notes
			b[8]=r.storage_in_id	
			b[9]=r.create_time
			b[10]=r.supplier
			b[11]=r.total_fee_sum
			b[12]=r.deliveryman
			b[13]=r.storeman
			b[14]=r.id	
			a[i]=b
			i=i+1
		return render_to_response("storage_storage_in_show.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})

@csrf_exempt
def modify_storage_in(request):
	storage_in_id = request.POST.get('storage_in_id', None)
	create_time = request.POST.get('create_time', None)
	supplier = request.POST.get('supplier', None)
	material_name = request.POST.get('material_name', None)
	size = request.POST.get('size', None)
	seller = request.POST.get('seller', None)
	amount = request.POST.get('amount', None)
	price = request.POST.get('price', None)
	total_fee = request.POST.get('total_fee', None)	
	notes = request.POST.get('notes', None)			
	total_fee_sum = request.POST.get('total_fee_sum', None)
	deliveryman = request.POST.get('deliveryman', None)
	storeman = request.POST.get('storeman', None)
	id = request.POST.get('id', None)
	try:
		Storage_in.objects.filter(id=id).update(create_time=create_time,supplier=supplier,material_name=material_name,size=size,seller=seller,amount=amount,price=price,total_fee=total_fee,notes=notes,total_fee_sum=total_fee_sum,deliveryman=deliveryman,storeman=storeman)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_storage_in(request):
	id = request.POST.get('id', None)
	try:
		Storage_in.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse("error", 500)
	return HttpResponse(json.dumps(1))

def storage_in_new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	temp=Storage_in.objects.all().order_by('-id')[0].id
	storage_in_id=int(temp)+1
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		return render_to_response("storage_storage_in_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"storage_in_id":storage_in_id})

#api
@csrf_exempt
def fill_storage_in(request):
	storage_in_id = request.POST.get('storage_in_id', None)
	total_fee_sum = request.POST.get('total_fee_sum', None)	
	supplier = request.POST.get('supplier', None)			
	create_time = request.POST.get('create_time', None)
	deliveryman = request.POST.get('deliveryman', None)	
	storeman = request.POST.get('storeman', None)			
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	try:
		q = Storage_in(create_time=create_time,
				deliveryman=deliveryman,
				storeman=storeman,
				storage_in_id=storage_in_id,
				supplier=supplier,
				total_fee_sum=total_fee_sum,
				material_name=col1,
				size=col2,
				seller=col3,	
				amount=col4,
				price=col5,
				total_fee=col6,
				notes=col7)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	try:
		q = Storage_material(in_time=create_time,
			material_name=col1,
			size=col2,
			seller=col3,	
			amount=col4,
			price=col5,
			total_fee=col6,
			notes=col7)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error2', 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def get_storage_inID_by_product(request):
	material_name = request.POST.get('material_name', None)
	r=Storage_in.objects.filter(material_name=material_name)[0].storage_in_id
	return HttpResponse(json.dumps(r))

#################################################################
def storage_out(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Storage_out.objects.all()
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.storage_out_id
			b[1]=r.material_name
			b[2]=r.create_time
			b[3]=r.buyer
			b[4]=r.amount
			b[5]=r.total_fee	
			a[i]=b
			i=i+1
		return render_to_response("storage_storage_out.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})

def storage_out_show(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Storage_out.objects.filter(storage_out_id=id)
		a={}
		i=0
		for r in records:
			b={}
			b[0]=int(i+1)
			b[1]=r.material_name
			b[2]=r.size
			b[3]=r.buyer
			b[4]=r.amount
			b[5]=r.price		
			b[6]=r.total_fee
			b[7]=r.notes
			b[8]=r.storage_out_id	
			b[9]=r.create_time
			b[10]=r.customer
			b[11]=r.total_fee_sum
			b[12]=r.deliveryman
			b[13]=r.storeman
			b[14]=r.id	
			a[i]=b
			i=i+1
		return render_to_response("storage_storage_out_show.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})

@csrf_exempt
def modify_storage_out(request):
	storage_out_id = request.POST.get('storage_out_id', None)
	create_time = request.POST.get('create_time', None)
	customer = request.POST.get('customer', None)
	material_name = request.POST.get('material_name', None)
	size = request.POST.get('size', None)
	buyer = request.POST.get('buyer', None)
	amount = request.POST.get('amount', None)
	price = request.POST.get('price', None)
	total_fee = request.POST.get('total_fee', None)	
	notes = request.POST.get('notes', None)			
	total_fee_sum = request.POST.get('total_fee_sum', None)
	deliveryman = request.POST.get('deliveryman', None)
	storeman = request.POST.get('storeman', None)
	id = request.POST.get('id', None)
	try:
		Storage_out.objects.filter(id=id).update(create_time=create_time,customer=customer,material_name=material_name,size=size,buyer=buyer,amount=amount,price=price,total_fee=total_fee,notes=notes,total_fee_sum=total_fee_sum,deliveryman=deliveryman,storeman=storeman)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_storage_out(request):
	id = request.POST.get('id', None)
	try:
		Storage_out.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse("error", 500)
	return HttpResponse(json.dumps(1))

def storage_out_new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	temp=Storage_out.objects.all().order_by('-id')[0].id
	storage_out_id=int(temp)+1
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		return render_to_response("storage_storage_out_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'storage_out_id':storage_out_id})

#api
@csrf_exempt
def fill_storage_out(request):
	storage_out_id = request.POST.get('storage_out_id', None)
	total_fee_sum = request.POST.get('total_fee_sum', None)	
	customer = request.POST.get('customer', None)			
	create_time = request.POST.get('create_time', None)
	deliveryman = request.POST.get('deliveryman', None)	
	storeman = request.POST.get('storeman', None)			
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	try:
		q = Storage_out(create_time=create_time,
				deliveryman=deliveryman,
				storeman=storeman,
				storage_out_id=storage_out_id,
				customer=customer,
				total_fee_sum=total_fee_sum,
				material_name=col1,
				size=col2,
				buyer=col3,	
				amount=col4,
				price=col5,
				total_fee=col6,
				notes=col7)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	try:
		old_amount=Storage_material.objects.filter(material_name=col1)[0].amount
		new_amount=int(old_amount)-int(col4)
		new_total_fee=int(new_amount)*int(col5)
		Storage_material.objects.filter(material_name=col1).update(amount=new_amount,out_time=create_time,total_fee=new_total_fee)
		print old_amount
		print new_amount
		print new_total_fee
	except Exception, e:
		return comutils.baseresponse('system error2', 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def get_storage_outID_by_product(request):
	material_name = request.POST.get('material_name', None)
	r=Storage_out.objects.filter(material_name=material_name)[0].storage_out_id
	return HttpResponse(json.dumps(r))


######################################


def storage_material(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Storage_material.objects.all()
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.material_name
			b[1]=r.size	
			b[2]=r.seller
			b[3]=r.amount
			b[4]=r.price
			b[5]=r.total_fee
			b[6]=r.in_time
			b[7]=r.out_time
			b[8]=r.notes
			b[9]=r.id	
			b[10]=int(i+1)
			a[i]=b
			i=i+1
		return render_to_response("storage_storage_material.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})


@csrf_exempt
def modify_material(request):
	material_name = request.POST.get('material', None)
	size = request.POST.get('size', None)
	seller = request.POST.get('seller', None)
	amount = request.POST.get('amount', None)
	price = request.POST.get('price', None)
	total_fee = request.POST.get('total_fee', None)	
	notes = request.POST.get('notes', None)			
	in_time = request.POST.get('in_time', None)
	out_time = request.POST.get('out_time', None)
	id = request.POST.get('id', None)
	try:
		Storage_material.objects.filter(id=id).update(material_name=material_name,size=size,seller=seller,amount=amount,price=price,total_fee=total_fee,notes=notes,in_time=in_time,out_time=out_time)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_material(request):
	id = request.POST.get('id', None)
	try:
		Storage_material.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse("error", 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def get_details_by_material(request):
	material_name = request.POST.get('material_name', None)
	r=Storage_material.objects.filter(material_name=material_name)[0]
	b={}
	b[0]=r.material_name
	b[1]=r.size
	b[2]=r.seller
	b[3]=r.amount
	b[4]=r.price
	b[5]=r.total_fee
	b[6]=r.in_time
	b[7]=r.out_time
	b[8]=r.notes
	b[9]=r.id
	return HttpResponse(json.dumps(b))


######################################


@csrf_exempt
def modify_storage(request):
	productID = request.POST.get('productID', None)
	product_name = request.POST.get('product_name', None)	
	size = request.POST.get('size', None)			
	amount = request.POST.get('amount', None)
	in_time = request.POST.get('in_time', None)
	out_time = request.POST.get('out_time', None)
	customer = request.POST.get('customer', None)
	notes = request.POST.get('notes', None)
	try:
		Storage.objects.filter(productID=productID).update(customer=customer,product_name=product_name,size=size,amount=amount,in_time=in_time,out_time=out_time,notes=notes)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_storage(request):
	productID = request.POST.get('productID', None)
	try:
		Storage.objects.filter(productID=productID).delete()
	except Exception, e:
		return comutils.baseresponse("error", 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def get_storageID_by_product(request):
	product_name = request.POST.get('product_name', None)
	r=Storage.objects.filter(product_name=product_name)[0]
	b={}
	b[0]=r.customer
	b[1]=r.product_name
	b[2]=r.size
	b[3]=r.amount
	b[4]=r.in_time
	b[5]=r.out_time
	b[6]=r.notes
	b[7]=r.productID
	return HttpResponse(json.dumps(b))
#api
@csrf_exempt
def get_storageID_by_customer(request):
	customer = request.POST.get('customer', None)
	r=Storage.objects.filter(customer=customer)[0]
	b={}
	b[0]=r.customer
	b[1]=r.product_name
	b[2]=r.size
	b[3]=r.amount
	b[4]=r.in_time
	b[5]=r.out_time
	b[6]=r.notes
	b[7]=r.productID
	return HttpResponse(json.dumps(b))
