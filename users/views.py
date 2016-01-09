#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from users.models import User

def get_user_list(records):	
	a={}
	i=0
	for user in records:
		b={}
		b[0]=user.id
		b[1]=user.phone
		b[2]=user.nick_name
		b[3]=user.role
		b[5]=int(i+1)
		a[i]=b
		i=i+1
	return a

def list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		pk = request.session.get('pk',False)
		p = User.objects.filter(id=pk)[0].p8
		if int(p)==0:
			return HttpResponseRedirect("/denied")
		a={}
		records_all=User.objects.all()
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=User.objects.all().order_by('-id')
				a=get_user_list(records)
			else:
				records=User.objects.all().order_by('-id')[0:10]
				a=get_user_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=User.objects.all().order_by('-id')[last:]
				a=get_user_list(records)
			else:
				first=int(num-1)*10
				records=User.objects.all().order_by('-id')[first:int(first+10)]
				a=get_user_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("users_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'length':len(records),'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})

def new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p8
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		return render_to_response("users_new.html",{'is_login':json.dumps(is_login),'nick_name':nick_name})

def user(request,id):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		user = User.objects.filter(id=id)[0]
		b={}
		b[0]=user.id
		b[1]=user.phone
		b[2]=user.nick_name
		b[3]=user.qq
		b[4]=user.sexy
		b[5]=user.role
		b[6]=user.p1
		b[7]=user.p2
		b[8]=user.p3
		b[9]=user.p4
		b[10]=user.p5
		b[11]=user.p6
		b[12]=user.p7
		b[13]=user.p8
		b[14]=user.p9
		b[15]=user.p10
		return render_to_response("users_user.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':b})


#api
@csrf_exempt
def signin(request):

	phone = request.POST.get('phone', None)
	password = request.POST.get('password', None)

	try:
		userlist = User.objects.filter(phone=phone)
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	
	user=userlist[0]
	
	if not user:
		return comutils.baseresponse('user not found', 404)
	if password != user.signin_passwd:
		return comutils.baseresponse('password is not correct', 400)

	request.session['is_login'] = True
	request.session['pk'] = user.pk
	request.session['phone'] = user.phone
	request.session['nick_name'] = user.nick_name

	return HttpResponse(json.dumps(1))

#api
@csrf_exempt
def signup(request):

	phone = request.POST.get('phone', None)
	password = request.POST.get('password', None)
	nickname = request.POST.get('nickname', None)
	sexy = request.POST.get('sexy', None)
	qq = request.POST.get('qq', None)
	role = request.POST.get('role', None)
	p1 = request.POST.get('p1', None)
	p2 = request.POST.get('p2', None)
	p3 = request.POST.get('p3', None)
	p4 = request.POST.get('p4', None)
	p5 = request.POST.get('p5', None)
	p6 = request.POST.get('p6', None)
	p7 = request.POST.get('p7', None)
	p8 = request.POST.get('p8', None)
	p9 = request.POST.get('p9', None)
	p10 = request.POST.get('p10', None)

	try:
		user = User(phone = phone,
                nick_name = nickname,
                signin_passwd = password,
                sexy=sexy,
                qq=qq,
                role=role,
                p1=p1,
                p2=p2,
                p3=p3,
                p4=p4,
                p5=p5,
                p6=p6,
                p7=p7,
                p8=p8,
                p9=p9,
                p10=p10)
		user.save()
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))

@csrf_exempt
def delete_user(request):
	id=request.POST.get('id', None)
	try:
		User.objects.filter(id=id).delete()
	except Exception, e:
		return comutils.baseresponse('system error', 500)
	return HttpResponse(json.dumps(1))



#api
@csrf_exempt
def modify_user(request):
	id = request.POST.get('id', None)
	phone = request.POST.get('phone', None)
	password = request.POST.get('password', None)
	nickname = request.POST.get('nickname', None)
	sexy = request.POST.get('sexy', None)
	qq = request.POST.get('qq', None)
	role = request.POST.get('role', None)
	p1 = request.POST.get('p1', None)
	p2 = request.POST.get('p2', None)
	p3 = request.POST.get('p3', None)
	p4 = request.POST.get('p4', None)
	p5 = request.POST.get('p5', None)
	p6 = request.POST.get('p6', None)
	p7 = request.POST.get('p7', None)
	p8 = request.POST.get('p8', None)
	p9 = request.POST.get('p9', None)
	p10 = request.POST.get('p10', None)

	try:
		User.objects.filter(id=id).update(phone = phone,
                nick_name = nickname,
                signin_passwd = password,
                sexy=sexy,
                qq=qq,
                role=role,
                p1=p1,
                p2=p2,
                p3=p3,
                p4=p4,
                p5=p5,
                p6=p6,
                p7=p7,
                p8=p8,
                p9=p9,
                p10=p10)
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))

#api
@csrf_exempt
def get_id_by_username(request):
	nick_name = request.POST.get('user_search', None)
	r = User.objects.filter(nick_name=nick_name)
	if r:
		id=r[0].id
		return HttpResponse(id)
	else:
		return HttpResponse(json.dumps(0))





