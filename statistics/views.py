#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from storage.models import Storage,Storage_in,Storage_out,Storage_material

# Create your views here.
def get_statistics_list(records):	
	a={}
	i=0
	for r in records:
		b={}
		b[0]=r.product_name
		b[1]=r.material
		b[2]=r.daliao
		b[3]=r.size
		a[i]=b
		i=i+1
	return a

def statistics_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
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
				a=get_statistics_list(records)
			else:
				records=User.objects.all().order_by('-id')[0:10]
				a=get_statistics_list(records)
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=Process.objects.all().order_by('-id')[last:]
				a=get_statistics_list(records)
			else:
				first=int(num)*10
				records=Process.objects.all().order_by('-id')[first:int(first+10)]
				a=get_statistics_list(records)
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("statistics_statistics.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})


