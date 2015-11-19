#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker,Tracking


def tracking_list(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Tracking.objects.all()
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.product_name
			b[1]=r.customer
			b[2]=r.state
			b[3]=r.pipline_step		
			b[4]=r.create_time
			b[5]=r.deadline
			b[6]=r.notes	
			b[7]=r.productID
			b[8]=r.id
			b[9]=int(i+1)
			a[i]=b
			i=i+1
		return render_to_response("work_tracking.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'length':i})


@csrf_exempt
def get_details_by_ID(request):
	id = request.POST.get('id', None)
	try:
		r = Tracking.objects.filter(id=id)[0]
		b={}
		b[0]=r.product_name
		b[1]=r.customer
		b[2]=r.state
		b[3]=r.pipline_step		
		b[4]=r.create_time
		b[5]=r.deadline
		b[6]=r.notes	
		b[7]=r.productID
		b[8]=r.id
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(b))


@csrf_exempt
def modify_tracking(request):
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	col8 = request.POST.get('col8', None)
	id=request.POST.get('id', None)
	try:
		Tracking.objects.filter(id=id).update(product_name=col1,customer=col2,state=col3,pipline_step=col4,create_time=col6,deadline=col7,notes=col8)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))


#api
@csrf_exempt
def get_productID_by_product(request):
	product_name = request.POST.get('product_name', None)
	productID=Tracking.objects.filter(product_name=product_name)[0].productID
	if(len(productID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(productID)


@csrf_exempt
def get_productID_by_customer(request):
	customer = request.POST.get('customer', None)
	productID=Tracking.objects.filter(customer=customer)[0].productID
	if(len(productID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(productID)

###############

def tracking(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Tracking.objects.filter(productID=id)
		a={}
		i=0
		for r in records:
			b={}
			b[0]=r.product_name
			b[1]=r.customer
			b[2]=r.state
			b[3]=r.pipline_step		
			b[4]=r.create_time
			b[5]=r.deadline
			b[6]=r.notes	
			b[7]=r.productID
			b[8]=r.id
			b[9]=int(i+1)
			a[i]=b
			i=i+1
		return render_to_response("work_tracking_one.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})

@csrf_exempt
def delete_tracking(request):
	id=request.POST.get('id', None)
	try:
		Tracking.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))


############## 


def worker(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Worker.objects.all().order_by('-id')
		a={}
		i=0
		for w in records:
			b={}
			b[0]=w.workerID
			b[1]=w.worker_name
			b[2]=w.product_name
			b[3]=w.pipline_step
			b[4]=w.count
			b[5]=w.salary
			b[6]=w.create_time
			b[7]=w.notes
			b[8]=w.productID
			b[9]=w.id
			b[10]=int(i+1)
			a[i]=b
			i=i+1
		return render_to_response("work_worker.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'length':i})

@csrf_exempt
def get_workerdetails_by_ID(request):
	id = request.POST.get('id', None)
	try:
		r = Worker.objects.filter(id=id)[0]
		b={}
		b[0]=r.worker_name
		b[1]=r.product_name
		b[2]=r.pipline_step
		b[3]=r.count
		b[4]=r.salary
		b[5]=r.create_time
		b[6]=r.notes
		b[7]=r.id
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(b))


@csrf_exempt
def modify_worker(request):
	col1 = request.POST.get('col1', None)
	col2 = request.POST.get('col2', None)
	col3 = request.POST.get('col3', None)
	col4 = request.POST.get('col4', None)
	col5 = request.POST.get('col5', None)
	col6 = request.POST.get('col6', None)
	col7 = request.POST.get('col7', None)
	id=request.POST.get('id', None)
	try:
		Worker.objects.filter(id=id).update(worker_name=col1,product_name=col2,pipline_step=col3,count=col4,salary=col5,create_time=col6,notes=col7)
	except Exception, e:
		return comutils.baseresponse(e, 500)
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_worker(request):
	id=request.POST.get('id', None)
	try:
		Worker.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))


@csrf_exempt
def get_workerID_by_worker(request):
	worker_name = request.POST.get('worker_name', None)
	workerID=Worker.objects.filter(worker_name=worker_name)[0].workerID
	if(len(workerID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(workerID)


@csrf_exempt
def get_workerID_by_product(request):
	product_name = request.POST.get('product_name', None)
	workerID=Worker.objects.filter(product_name=product_name)[0].workerID
	if(len(workerID)==0):
		return HttpResponse(0)
	else:
		return HttpResponse(workerID)



######################################
def worker_worker(request,workerID):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Worker.objects.filter(workerID=workerID)
		a={}
		i=0
		for w in records:
			b={}
			b[0]=w.workerID
			b[1]=w.worker_name
			b[2]=w.product_name
			b[3]=w.pipline_step
			b[4]=w.count
			b[5]=w.salary
			b[6]=w.create_time
			b[7]=w.notes
			b[8]=w.productID
			b[9]=w.id
			b[10]=int(i+1)
			a[i]=b
			i=i+1
		return render_to_response("work_worker_one.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'length':i})



#api
@csrf_exempt
def check_productID(request):
	productID = request.POST.get('productID', None)
	records=Process.objects.filter(productID=productID)
	if(len(records)==0):
		return HttpResponse(json.dumps(0))
	else:
		return HttpResponse(json.dumps(1))

