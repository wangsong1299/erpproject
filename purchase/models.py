from django.db import models

# Create your models here.
class Purchase(models.Model):
	productID=models.CharField(max_length = 10)
	customer=models.CharField(max_length = 30,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	process_step=models.CharField(max_length = 3,default=1)

class Purchase_single(models.Model):
	productID=models.CharField(max_length = 10)
	customer=models.CharField(max_length = 30,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	create_time=models.CharField(max_length = 30,blank = True)
	surface=models.CharField(max_length = 30,blank = True)
	material=models.CharField(max_length = 30,blank = True)
	daliao=models.CharField(max_length = 30,blank = True)
	size=models.CharField(max_length = 30,blank = True)
	wl_size=models.CharField(max_length = 30,blank = True)
	wl_size2=models.CharField(max_length = 30,blank = True)
	wl_feizhi=models.CharField(max_length = 30,blank = True)
	wl_thin=models.CharField(max_length = 30,blank = True)
	wl_biaoliao=models.CharField(max_length = 30,blank = True)
	wl_waleng=models.CharField(max_length = 30,blank = True)
	notes=models.CharField(max_length = 100,blank = True)


class Purchase_multiple(models.Model):
	productID=models.CharField(max_length = 10)
	product_name=models.CharField(max_length = 50,blank = True)
	price=models.CharField(max_length = 30,blank = True)
	amount=models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 30,blank = True)
	suppliers=models.CharField(max_length = 30,blank = True)
	contacts=models.CharField(max_length = 30,blank = True)
	contacts_phone=models.CharField(max_length = 11,blank = True)
	notes=models.CharField(max_length = 100,blank = True)
