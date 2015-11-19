#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from users.models import User


def list(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		users = User.objects.all()
		a={}
		i=0
		for user in users:
			b={}
			b[0]=user.id
			b[1]=user.phone
			b[2]=user.nick_name
			b[3]=user.role
			b[4]=user.department
			b[5]=int(i+1)
			a[i]=b
			i=i+1
		return render_to_response("users_list.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'length':i})

	
def new(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
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
		b[6]=user.department
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
	department = request.POST.get('department', None)
	permission = request.POST.get('permission', None)

	try:
		user = User(phone = phone,
                nick_name = nickname,
                signin_passwd = password,
                sexy=sexy,
                qq=qq,
                role=role,
                department=department,
                permission=permission)
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
	department = request.POST.get('department', None)
	permission = request.POST.get('permission', None)

	try:
		User.objects.filter(id=id).update(phone = phone,
                nick_name = nickname,
                signin_passwd = password,
                sexy=sexy,
                qq=qq,
                role=role,
                department=department,
                permission=permission)
	except Exception, e:
		return comutils.baseresponse('system error', 500)	
	return HttpResponse(json.dumps(1))



