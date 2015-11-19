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
def statistics(request):
	is_login=request.session.get('is_login',False)
	nick_name = request.session.get('nick_name',False)
	if not is_login:
		return HttpResponseRedirect("/")
	else:
		records=Process.objects.all()
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
		return render_to_response("statistics_statistics.html",{'is_login':json.dumps(is_login),'nick_name':nick_name,'records':a})
