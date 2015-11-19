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

# Create your views here.
def alert(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Process.objects.all().order_by('alerttime')
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
		return render_to_response("alert_alert.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})
