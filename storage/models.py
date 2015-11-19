from django.db import models

# Create your models here.
class Storage(models.Model):
	productID=models.CharField(max_length = 30)
	customer=models.CharField(max_length = 50)
	product_name=models.CharField(max_length = 50,blank=True)
	size=models.CharField(max_length = 30)
	amount=models.CharField(max_length = 30)
	in_time=models.CharField(max_length = 30)
	out_time=models.CharField(max_length = 30)
	notes=models.CharField(max_length = 30)


class Storage_in(models.Model):
	storage_in_id=models.CharField(max_length = 30,blank=True)
	material_id=models.CharField(max_length = 30,blank=True)
	create_time=models.CharField(max_length = 30,blank=True)
	supplier=models.CharField(max_length = 30,blank = True)
	material_name=models.CharField(max_length = 30,blank = True)
	seller=models.CharField(max_length = 30,blank = True)
	size=models.CharField(max_length = 30,blank = True)
	amount=models.CharField(max_length = 30,blank = True)
	price=models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 30,blank = True)
	notes=models.CharField(max_length = 30,blank = True)
	total_fee_sum=models.CharField(max_length = 30,blank = True)
	deliveryman=models.CharField(max_length = 30,blank = True)
	storeman=models.CharField(max_length = 30,blank = True)

class Storage_out(models.Model):
	storage_out_id=models.CharField(max_length = 30,blank=True)
	material_id=models.CharField(max_length = 30,blank=True)
	create_time=models.CharField(max_length = 30,blank = True)
	customer=models.CharField(max_length = 30,blank = True)
	material_name=models.CharField(max_length = 30,blank = True)
	buyer=models.CharField(max_length = 30,blank = True)
	size=models.CharField(max_length = 30,blank = True)
	amount=models.CharField(max_length = 30,blank = True)
	price=models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 30,blank = True)
	notes=models.CharField(max_length = 30,blank = True)
	total_fee_sum=models.CharField(max_length = 30,blank = True)
	deliveryman=models.CharField(max_length = 30,blank = True)
	storeman=models.CharField(max_length = 30,blank = True)

class Storage_material(models.Model):
	material_id=models.CharField(max_length = 30,blank=True)
	material_name=models.CharField(max_length = 30,blank=True)
	seller=models.CharField(max_length = 30,blank=True)
	size=models.CharField(max_length = 30,blank=True)
	amount=models.CharField(max_length = 30,blank=True)
	price=models.CharField(max_length = 30,blank=True)
	total_fee=models.CharField(max_length = 30,blank=True)
	in_time=models.CharField(max_length = 30,blank=True)
	out_time=models.CharField(max_length = 30,blank=True)
	notes=models.CharField(max_length = 30,blank=True)



