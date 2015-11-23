#! -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Quotation(models.Model):
	customer=models.CharField(max_length = 30)
	product_name=models.CharField(max_length = 30)
  	create_time = models.DateTimeField(auto_now_add = True, blank = True)
  	contacts=models.CharField(max_length = 30)
	contacts_phone=models.CharField(max_length = 11,default=0)

	total_fee=models.CharField(max_length = 11,default=0)
	
	material_price =models.CharField(max_length = 10,default=0)
	size_price=models.CharField(max_length = 10,default=0)
	wl_material_price=models.CharField(max_length = 10,default=0)
	amount_price=models.CharField(max_length = 10,default=0)
	print_fee_price=models.CharField(max_length = 12,default=0)
	print_color_price=models.CharField(max_length = 12,default=0)
	print_parts_price=models.CharField(max_length = 12,default=0)	
	surface_price=models.CharField(max_length = 10,default=0)
	tangjin_price=models.CharField(max_length = 12,default=0)
	safen_price=models.CharField(max_length = 12,default=0)
	packing_box_price=models.CharField(max_length = 12,default=0)
	packing_fee_price=models.CharField(max_length = 12,default=0)
	transportation_fee_price=models.CharField(max_length = 12,default=0)

	material =models.CharField(max_length = 10,blank = True)
	size=models.CharField(max_length = 10,blank = True)
	wl_material=models.CharField(max_length = 10,blank = True)
	amount=models.CharField(max_length = 10,blank = True)
	print_fee=models.CharField(max_length = 12,blank = True)
	print_color=models.CharField(max_length = 12,blank = True)
	print_parts=models.CharField(max_length = 12,blank = True)	
	surface=models.CharField(max_length = 10,blank = True)
	tangjin=models.CharField(max_length = 12,blank = True)
	safen=models.CharField(max_length = 12,blank = True)
	packing_box=models.CharField(max_length = 12,blank = True)
	packing_fee=models.CharField(max_length = 12,blank = True)
	transportation_fee=models.CharField(max_length = 12,blank = True)


class Order(models.Model):
	productID=models.CharField(max_length = 10,unique=True)
	customer=models.CharField(max_length = 30,default=0)
	contacts=models.CharField(max_length = 30,default=0)
	contacts_phone=models.CharField(max_length = 11,default=0)
	fax=models.CharField(max_length = 15,blank = True)
	qq=models.CharField(max_length = 12,blank = True)
	create_time=models.CharField(max_length = 12,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	amount=models.CharField(max_length = 30)
	price=models.CharField(max_length = 10,blank = True)
	fee=models.CharField(max_length = 10,blank = True)
	edition_fee =models.CharField(max_length = 10,blank = True)
	total_fee=models.CharField(max_length = 10,default=0)
	deadline = models.CharField(max_length = 20,blank = True)
	feilin=models.CharField(max_length = 30,blank = True)
	material=models.CharField(max_length = 30,blank = True)
	size=models.CharField(max_length = 30,blank = True)
	surface=models.CharField(max_length = 30,blank = True)
	wl_material=models.CharField(max_length = 30,blank = True)
	wl_kind=models.CharField(max_length = 30,blank = True)
	mould=models.CharField(max_length = 30,blank = True)
	notes=models.CharField(max_length = 30,blank = True)
	delivery_address=models.CharField(max_length = 30,blank = True)
	productID2=models.CharField(max_length = 30,blank = True)
	call=models.CharField(max_length = 30,blank = True)

class Delivery(models.Model):
	deliveryID=models.CharField(max_length = 10)
	choice=models.CharField(max_length = 10,default=1)
	delivery_name=models.CharField(max_length = 30,blank = True)
	delivery_time=models.CharField(max_length = 50,blank = True)
	productID=models.CharField(max_length = 10)
	product_name=models.CharField(max_length = 30,blank = True)
	order_amount =models.CharField(max_length = 30,blank = True)
	delivery_amount =models.CharField(max_length = 30,blank = True)
	price=models.CharField(max_length = 30,blank = True)
	fee=models.CharField(max_length = 11,blank = True)
	notes=models.CharField(max_length = 15,blank = True)
	delivery_address=models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 30,blank = True)
	receive_man=models.CharField(max_length = 15,blank = True)
	delivery_man=models.CharField(max_length = 15,blank = True)
	send_name=models.CharField(max_length = 15,blank = True)
	purchase_man=models.CharField(max_length = 15,blank = True)
	product_number=models.CharField(max_length = 15,blank = True)
	perbox=models.CharField(max_length = 15,blank = True)
	box=models.CharField(max_length = 15,blank = True)
	send_phone=models.CharField(max_length = 30,blank = True)
	send_fax=models.CharField(max_length = 15,blank = True)
	receive_phone=models.CharField(max_length = 15,blank = True)
	receive_fax=models.CharField(max_length = 15,blank = True)
	huoID=models.CharField(max_length = 15,blank = True)
	inner_amount=models.CharField(max_length = 15,blank = True)
	outer_amount=models.CharField(max_length = 15,blank = True)
	total_notes=models.CharField(max_length = 15,blank = True)

class Process(models.Model):
	productID=models.CharField(max_length = 10)
	customer =models.CharField(max_length = 30,blank = True)
	create_time=models.CharField(max_length = 30,blank = True)
	deadline=models.CharField(max_length = 11,blank = True)
	alerttime=models.CharField(max_length = 11,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	number_1=models.CharField(max_length = 15,blank = True)
	number_2=models.CharField(max_length = 12,blank = True)
	amount=models.CharField(max_length = 30,default=0)
	pinban=models.CharField(max_length = 10,blank = True)
	yinshu=models.CharField(max_length = 10,blank = True)
	yinsha =models.CharField(max_length = 10,blank = True)
	jiayinshu=models.CharField(max_length = 10,blank = True)
	zhenjiao = models.CharField(max_length = 20,blank = True)
	total_yinshu=models.CharField(max_length = 30,blank = True)
	yaheng=models.CharField(max_length = 30,blank = True)
	lingyin=models.CharField(max_length = 30,blank = True)
	surface=models.CharField(max_length = 30,blank = True)
	process=models.CharField(max_length = 2,blank = True)
	notes=models.CharField(max_length = 30,blank = True)
	material=models.CharField(max_length = 30,blank = True)
	daliao=models.CharField(max_length = 30,blank = True)
	size=models.CharField(max_length = 30,blank = True)
	kaishu=models.CharField(max_length = 30,blank = True)
	kaiyin=models.CharField(max_length = 30,blank = True)
	fudai=models.CharField(max_length = 30,blank = True)
	quality=models.CharField(max_length = 100,blank = True)
	wl_size=models.CharField(max_length = 30,blank = True)
	wl_size2=models.CharField(max_length = 30,blank = True)
	wl_feizhi=models.CharField(max_length = 30,blank = True)
	wl_thin=models.CharField(max_length = 30,blank = True)
	wl_waleng=models.CharField(max_length = 30,blank = True)
	wl_biaoliao=models.CharField(max_length = 30,blank = True)
	finished=models.CharField(max_length = 2,default=0)



class Cost(models.Model):
	productID=models.CharField(max_length = 10)
	customer =models.CharField(max_length = 30,blank = True)
	create_time=models.CharField(max_length = 30,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	surface=models.CharField(max_length = 30,blank = True)
	material=models.CharField(max_length = 30,blank = True)
	wl_feizhi=models.CharField(max_length = 30,blank = True)
	wl_waleng=models.CharField(max_length = 30,blank = True)
	daliao=models.CharField(max_length = 30,blank = True)
	size=models.CharField(max_length = 30,blank = True)
	surface_price=models.CharField(max_length = 30,blank = True)
	material_price=models.CharField(max_length = 30,blank = True)
	wl_feizhi_price=models.CharField(max_length = 30,blank = True)
	wl_waleng_price=models.CharField(max_length = 30,blank = True)
	worker_fee=models.CharField(max_length = 15,blank = True)
	other_fee=models.CharField(max_length = 15,blank = True)	
	notes =models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 30,blank = True)
	
class Image(models.Model):
    productID = models.CharField(max_length = 30)
    productImg = models.FileField(upload_to = './upload/')

