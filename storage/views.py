#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from storage.models import Storage,Storage_in,Storage_out,Storage_material
from users.models import User

def get_storage_list(records):	
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
		b[9]=r.id
		a[i]=b
		i=i+1
	return a

def storage_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p3
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Storage.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Storage.objects.all().order_by('-id')
				a=get_storage_list(records)
			else:
				records=Storage.objects.all().order_by('-id')[0:10]
				a=get_storage_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Storage.objects.all().order_by('-id')[last:]
				a=get_storage_list(records)
			else:
				first=int(num-1)*10
				records=Storage.objects.all().order_by('-id')[first:int(first+10)]
				a=get_storage_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		jc=False
		return render_to_response("storage_storage.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click),'jc':json.dumps(jc)})

def storage_c(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		customer=Storage.objects.filter(id=id)[0].customer
		records=Storage.objects.filter(customer=customer)
		a=get_storage_list(records)
		pre_click=False
		later_click=False
		jc=True
		return render_to_response("storage_storage.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click),'jc':json.dumps(jc)})

def storage_p(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		product_name=Storage.objects.filter(id=id)[0].product_name
		records=Storage.objects.filter(product_name=product_name)
		a=get_storage_list(records)
		pre_click=False
		later_click=False
		jc=True
		return render_to_response("storage_storage.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click),'jc':json.dumps(jc)})

def storage(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		r=Storage.objects.filter(id=num)[0]
		b={}
		b[0]=r.customer
		b[1]=r.product_name
		b[2]=r.size
		b[3]=r.amount
		b[4]=r.in_time
		b[5]=r.out_time
		b[6]=r.notes
		b[7]=r.productID
		b[8]=r.id
		return render_to_response("storage_storage_one.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b})

#################################################################
def get_storageIn_list(records):	
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
	return a

def storage_in_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p3
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Storage_in.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Storage_in.objects.all().order_by('-id')
				a=get_storageIn_list(records)
			else:
				records=Storage_in.objects.all().order_by('-id')[0:10]
				a=get_storageIn_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Storage_in.objects.all().order_by('-id')[last:]
				a=get_storageIn_list(records)
			else:
				first=int(num-1)*10
				records=Storage_in.objects.all().order_by('-id')[first:int(first+10)]
				a=get_storageIn_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("storage_storage_in.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})

def storage_in_p(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		material_name=Storage_in.objects.filter(storage_in_id=id)[0].material_name
		records=Storage_in.objects.filter(material_name=material_name)
		a=get_storageIn_list(records)
		inflag=True
		outflag=False	
		return render_to_response("storage_search_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'inflag':json.dumps(inflag),'outflag':json.dumps(outflag)})

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
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		r = Storage_in.objects.all().order_by('-id')
		if r:
			temp=r[0].id
			storage_in_id=int(temp)+1
		else:
			storage_in_id=1
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
	r=Storage_in.objects.filter(material_name=material_name)
	if r:
		id=r[0].storage_in_id
		return HttpResponse(id)
	else:
		return HttpResponse(0)

#################################################################
def get_storageOut_list(records):	
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
	return a

def storage_out_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p3
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Storage_out.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Storage_out.objects.all().order_by('-id')
				a=get_storageOut_list(records)
			else:
				records=Storage_out.objects.all().order_by('-id')[0:10]
				a=get_storageOut_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Storage_out.objects.all().order_by('-id')[last:]
				a=get_storageOut_list(records)
			else:
				first=int(num-1)*10
				records=Storage_out.objects.all().order_by('-id')[first:int(first+10)]
				a=get_storageOut_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("storage_storage_out.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})

def storage_out_p(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		material_name=Storage_out.objects.filter(storage_out_id=id)[0].material_name
		records=Storage_out.objects.filter(material_name=material_name)
		a=get_storageOut_list(records)
		inflag=False
		outflag=True	
		print inflag,outflag
		return render_to_response("storage_search_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'inflag':json.dumps(inflag),'outflag':json.dumps(outflag)})

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
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		r = Storage_out.objects.all().order_by('-id')
		if r:
			temp=r[0].id
			storage_out_id=int(temp)+1
		else:
			storage_out_id=1
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
	r=Storage_material.objects.filter(material_name=col1)
	if not r:
		return comutils.baseresponse('没有该种原料', 500)
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
	r =Storage_out.objects.filter(material_name=material_name).order_by('-id')
	if r:
		id=r[0].storage_out_id
		return HttpResponse(id)
	else:
		return HttpResponse(0)


######################################

def get_storageMaterial_list(records):	
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
	return a

def storage_material_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p3
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records_all=Storage_material.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=Storage_material.objects.all().order_by('-id')
				a=get_storageMaterial_list(records)
			else:
				records=Storage_material.objects.all().order_by('-id')[0:10]
				a=get_storageMaterial_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Storage_material.objects.all().order_by('-id')[last:]
				a=get_storageMaterial_list(records)
			else:
				first=int(num-1)*10
				records=Storage_material.objects.all().order_by('-id')[first:int(first+10)]
				a=get_storageMaterial_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("storage_storage_material.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})

def storage_material(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		r=Storage_material.objects.filter(id=num)[0]
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
		return render_to_response("storage_storage_material_one.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":b})


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
	r=Storage_material.objects.filter(material_name=material_name)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)

######################################


@csrf_exempt
def modify_storage(request):
	id = request.POST.get('id', None)
	product_name = request.POST.get('product_name', None)	
	size = request.POST.get('size', None)			
	amount = request.POST.get('amount', None)
	in_time = request.POST.get('in_time', None)
	out_time = request.POST.get('out_time', None)
	customer = request.POST.get('customer', None)
	notes = request.POST.get('notes', None)
	try:
		Storage.objects.filter(id=id).update(customer=customer,product_name=product_name,size=size,amount=amount,in_time=in_time,out_time=out_time,notes=notes)
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
	r=Storage.objects.filter(product_name=product_name)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)


#api
@csrf_exempt
def get_storageID_by_customer(request):
	customer = request.POST.get('customer', None)
	r=Storage.objects.filter(customer=customer)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(0)


#api
@csrf_exempt
def get_storagedetails_by_piplineID(request):
	id = request.POST.get('id', None)
	r=Storage.objects.filter(id=id)[0]
	b={}
	b[0]=r.customer
	b[1]=r.product_name
	b[2]=r.size
	b[3]=r.amount
	b[4]=r.in_time
	b[5]=r.out_time
	b[6]=r.notes
	b[7]=r.productID
	b[8]=r.id
	return HttpResponse(json.dumps(b))

#api
@csrf_exempt
def get_materialdetails_by_piplineID(request):
	id = request.POST.get('id', None)
	r=Storage_material.objects.filter(id=id)[0]
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


