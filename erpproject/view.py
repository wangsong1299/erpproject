# coding: utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from sales.models import Quotation,Order,Process,Delivery,Cost,Image
from work.models import Worker,Tracking
from users.models import User
from users import utils as comutils
import datetime
import sys
from django import forms

reload(sys)
sys.setdefaultencoding('utf8')

class UserForm(forms.Form):
    id = forms.CharField()
    headImg = forms.FileField()

#iframe 
def barcode(request,code):
	print code
	return render_to_response('barcode.html',{'code':code});

def upload_iframe(request,id):
	uf = UserForm()
	return render_to_response('upload.html',{'uf':uf,'id':id});

def upload_show(request,id):
	r=Image.objects.filter(productID=id)
	if r:
		productImg=r[0].productImg
		return render_to_response('upload_show.html',{'productImg':productImg});
	else:
		productImg=0
		return render_to_response('upload_show.html',{'productImg':productImg});

@csrf_exempt
def upload(request):
	if request.method == "POST":
		uf = UserForm(request.POST,request.FILES)
		if uf.is_valid():
			productID = uf.cleaned_data['id']
			productImg = uf.cleaned_data['headImg']
			user = Image()
			user.productID = productID
			print productID
			user.productImg = productImg
			print productImg
			user.save()
			return HttpResponse('上传完成!')

#normal
def index(request):
	is_login=request.session.get('is_login',False)
	if is_login:
		return render_to_response('index.html');
	else:	
		return render_to_response('signin.html');

def logout(request):
	request.session['is_login']=False
	return HttpResponseRedirect("/")


def api_test(request):
	is_login=request.session.get('is_login',False)
	uf = UserForm()
	return render_to_response('test.html',{'is_login':json.dumps(is_login),'uf':uf});


@csrf_exempt
def get_process_info(request):
	productID = request.POST.get('productID', None)
	try:
		r = Process.objects.filter(productID=productID)[0]
		b={}
		b[0]=r.productID
		b[1]=r.product_name
		b[2]=r.customer
		b[3]=r.amount
		b[4]=r.create_time
		b[5]=r.deadline
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(b))

@csrf_exempt
def count_work(request):
	workerID = request.POST.get('workerID', None)
	worker_name = request.POST.get('worker_name', None)
	productID = request.POST.get('productID', None)
	product_name = request.POST.get('product_name', None)
	pipline_step = request.POST.get('pipline_step', None)
	count = request.POST.get('count', None)
	notes = request.POST.get('notes', None)

	try:
		p = Worker(productID=productID,workerID=workerID,worker_name=worker_name,product_name=product_name,pipline_step=pipline_step,count=count,notes=notes)
		p.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))
	
@csrf_exempt
def login_in(request):
	phone = request.POST.get('phone', None)
	password = request.POST.get('password', None)
	user=User.objects.filter(phone=phone)[0]
	if not user:
		return comutils.baseresponse('用户不存在', 404)
	if password != user.signin_passwd:
		return comutils.baseresponse('密码不正确', 404)
	b={}
	b[0]=1
	b[1]=user.phone
	b[2]=user.nick_name
	b[3]=user.role
	b[4]=user.department
	return HttpResponse(json.dumps(b))

@csrf_exempt
def modify_password(request):
	phone = request.POST.get('phone', None)
	password = request.POST.get('old_password', None)
	new_password = request.POST.get('new_password', None)
	user=User.objects.filter(phone=phone)[0]
	if not user:
		return comutils.baseresponse('用户不存在', 404)
	if password != user.signin_passwd:
		return comutils.baseresponse('密码不正确', 404)
	user.signin_passwd=new_password
	return HttpResponse(json.dumps(1))

