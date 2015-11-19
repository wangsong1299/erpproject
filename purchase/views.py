#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from purchase.models import Purchase_single,Purchase_multiple
from customer.models import Supplier
def choice(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		return render_to_response("purchase_choice.html",{'is_login':json.dumps(is_login),'nick_name':nick_name})

def fill(request,productID):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		p=Process.objects.filter(productID=productID)[0]
		process_step=int(p.process)
		records={}
		if(process_step==1):
			records[0]=p.customer
			records[1]=p.product_name
			records[2]=p.create_time
			records[3]=p.surface
			records[4]=p.material
			records[5]=p.daliao
			records[6]=p.size
			records[7]=p.wl_size
			records[8]=p.wl_size2
			records[9]=p.wl_thin
			records[10]=p.wl_feizhi
			records[11]=p.wl_waleng
			records[12]=p.wl_biaoliao
			records[13]=p.notes
		return render_to_response("purchase_fill.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'process_step':process_step,'records':records,'productID':productID})

def search(request,productID):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		q=Process.objects.filter(productID=productID)[0]
		process_step=int(q.process)
		single_records={}
		multiple_records={}
		i=0
		if(process_step==1):
			p=Purchase_single.objects.filter(productID=productID)[0]		
			single_records[0]=p.customer
			single_records[1]=p.product_name
			single_records[2]=p.surface
			single_records[3]=p.create_time
			single_records[4]=p.material
			single_records[5]=p.daliao
			single_records[6]=p.size
			single_records[7]=p.wl_size
			single_records[8]=p.wl_size2
			single_records[9]=p.wl_thin
			single_records[10]=p.wl_feizhi
			single_records[11]=p.wl_waleng
			single_records[12]=p.wl_biaoliao
			single_records[13]=p.notes
			return render_to_response("purchase_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'process_step':process_step,'records':single_records,'productID':productID,'length':0})
		else:
			muls=Purchase_multiple.objects.filter(productID=productID)
			for m in muls:
				a={}
				a[0]=m.product_name
				a[1]=m.price
				a[2]=m.amount
				a[3]=m.total_fee
				a[4]=m.suppliers
				a[5]=m.contacts
				a[6]=m.contacts_phone
				a[7]=m.notes
				a[8]=int(i)+1
				multiple_records[i]=a
				i=i+1
			print multiple_records
			return render_to_response("purchase_search.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'process_step':process_step,'records':multiple_records,'productID':productID,'length':i})
	



#api
@csrf_exempt
def get_productID_by_product(request):
	product_name = request.POST.get('product_name', None)
	productID=Process.objects.filter(product_name=product_name)[0].productID
	if(len(productID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(productID)

@csrf_exempt
def get_productID_by_customer(request):
	customer = request.POST.get('customer', None)
	print customer
	productID=Process.objects.filter(customer=customer)[0].productID
	if(len(productID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(productID)


@csrf_exempt
def fill_single(request):
	productID = request.POST.get('productID', None)	
	customer = request.POST.get('customer', None)
	create_time = request.POST.get('create_time', None)
	product_name = request.POST.get('product_name', None)
	surface = request.POST.get('surface', None)
	notes = request.POST.get('notes', None)
	material = request.POST.get('material', None)	
	daliao = request.POST.get('daliao', None)
	size = request.POST.get('size', None)
	wl_biaoliao = request.POST.get('wl_biaoliao', None)
	wl_size = request.POST.get('wl_size', None)
	wl_size2 = request.POST.get('wl_size2', None)
	wl_feizhi = request.POST.get('wl_feizhi', None)
	wl_thin = request.POST.get('wl_thin', None)
	wl_waleng = request.POST.get('wl_waleng', None)

	try:
		q = Purchase_single(productID=productID,
				customer = customer,
				create_time=create_time,
				product_name=product_name,	
				surface=surface,
				notes=notes,
				material=material,
				daliao=daliao,      
				size=size,
				wl_size=wl_size,
				wl_size2=wl_size2,
				wl_thin=wl_thin,
				wl_feizhi=wl_feizhi,
				wl_biaoliao=wl_biaoliao,
				wl_waleng=wl_waleng)
		q.save()
	except Exception, e:
		return comutils.baseresponse(e, 500)
	
	return HttpResponse(json.dumps(1))


@csrf_exempt
def fill_multiple(request):
	productID = request.POST.get('productID', None)
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	col8 = request.POST.get('col8', None)
	try:
		q = Purchase_multiple(productID=productID,
				product_name=col1,
				price=col2,
				amount=col3,	
				total_fee=col4,
				suppliers=col5,
				contacts=col6,
				contacts_phone=col7,      
				notes=col8)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	try:
		q = Supplier(productID=productID,
				suppliers=col5,
				contacts=col6,
				contacts_phone=col7,      
				material_name=col1,
				price=col2,
				amount=col3,	
				total_fee=col4,
				notes=col8)
		q.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))


@csrf_exempt
def delete_single(request):
	productID = request.POST.get('productID', None)
	try:
		Purchase_single.objects.filter(productID=productID)[0].delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_multiple(request):
	productID = request.POST.get('productID', None)
	try:
		Purchase_multiple.objects.filter(productID=productID).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))


#修改

@csrf_exempt
def modify_single(request):
	productID = request.POST.get('productID', None)	
	customer = request.POST.get('customer', None)
	create_time = request.POST.get('create_time', None)
	product_name = request.POST.get('product_name', None)
	surface = request.POST.get('surface', None)
	notes = request.POST.get('notes', None)
	material = request.POST.get('material', None)	
	daliao = request.POST.get('daliao', None)
	size = request.POST.get('size', None)
	wl_biaoliao = request.POST.get('wl_biaoliao', None)
	wl_size = request.POST.get('wl_size', None)
	wl_size2 = request.POST.get('wl_size2', None)
	wl_feizhi = request.POST.get('wl_feizhi', None)
	wl_thin = request.POST.get('wl_thin', None)
	wl_waleng = request.POST.get('wl_waleng', None)

	try:
		Purchase_single.objects.filter(productID=productID).update(productID=productID,
				customer = customer,
				create_time=create_time,
				product_name=product_name,	
				surface=surface,
				notes=notes,
				material=material,
				daliao=daliao,      
				size=size,
				wl_size=wl_size,
				wl_size2=wl_size2,
				wl_thin=wl_thin,
				wl_feizhi=wl_feizhi,
				wl_biaoliao=wl_biaoliao,
				wl_waleng=wl_waleng)
	except Exception, e:
		return comutils.baseresponse(e, 500)	
	return HttpResponse(json.dumps(1))

@csrf_exempt
def modify_multiple(request):
	productID = request.POST.get('productID', None)
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	col8 = request.POST.get('col8', None)
	try:
		Purchase_multiple.objects.filter(productID=productID).update(productID=productID,
				product_name=col1,
				price=col2,
				amount=col3,	
				total_fee=col4,
				suppliers=col5,
				contacts=col6,
				contacts_phone=col7,      
				notes=col8)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))

