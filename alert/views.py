#! -*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from users import utils as comutils
from sales.models import Quotation,Order,Process,Delivery,Cost
from work.models import Worker
from storage.models import Storage,Storage_in,Storage_out,Storage_material
import datetime
from users.models import User
from django.utils.timezone import now, timedelta
# Create your views here.
def get_alert_list(records):
	c={}	
	a={}
	i=0
	for r in records:
		alert_date=r.alerttime
		split_date=alert_date.split("-")
		d1 = datetime.datetime(int(split_date[0]),int(split_date[1]),int(split_date[2]))  
		totay_date = datetime.datetime.now() 
		totay_date = totay_date.strftime('%Y-%m-%d') 
		split_date2 = totay_date.split("-")
		d2 = datetime.datetime(int(split_date2[0]),int(split_date2[1]),int(split_date2[2]))  
		if(d2<=d1):
			b={}
			b[0]=r.product_name
			b[1]=r.customer
			b[2]=r.alerttime
			b[3]=r.deadline
			b[4]=int(i+1)
			a[i]=b
			i=i+1
	c[0]=i
	c[1]=a
	return c

def alert_list(request,num):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	pk = request.session.get('pk',False)
	p = User.objects.filter(id=pk)[0].p10
	if int(p)==0:
		return HttpResponseRedirect("/denied")
	a={}
	pre_click=False
	later_click=False
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		start = now().date() + timedelta(days=-1)
		records_all=Process.objects.filter(alerttime__gt=start)
		page_all=int(len(records_all)-1)/10+1
		num=int(num)
		if(num==1):			
			if((len(records_all)<11)):	
				records=records_all.order_by('alerttime')
				rec = get_alert_list(records)
				a=rec[1]
				records_value_num=rec[0]
			else:
				records=records_all.order_by('alerttime')[0:10]
				rec = get_alert_list(records)
				a=rec[1]
				records_value_num=rec[0]
		else:
			if(num==page_all):
				last=int(page_all-1)*10
				records=records_all.order_by('alerttime')[last:]
				rec = get_alert_list(records)
				a=rec[1]
				records_value_num=rec[0]
			else:
				first=int(num-1)*10
				records=records_all.order_by('alerttime')[first:int(first+10)]
				rec = get_alert_list(records)
				a=rec[1]
				records_value_num=rec[0]
		if(num>1):
			pre_click=True
		if(num<int(page_all)):
			later_click=True
		return render_to_response("alert_alert.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,"records":a,'pre_click':json.dumps(pre_click),'later_click':json.dumps(later_click)})
