from django.db import models

# Create your models here.
class Customer(models.Model):
	productID=models.CharField(max_length = 10)
	customers=models.CharField(max_length = 30,blank = True)
	contacts=models.CharField(max_length = 30,blank = True)
	contacts_phone=models.CharField(max_length = 11,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	amount=models.CharField(max_length = 30)
	price=models.CharField(max_length = 10,blank = True)
	total_fee=models.CharField(max_length = 10,blank = True)
	create_time=models.CharField(max_length = 30,blank = True)
	notes=models.CharField(max_length = 30,blank = True)

class Supplier(models.Model):
	productID=models.CharField(max_length = 10)
	suppliers=models.CharField(max_length = 30,blank = True)
	contacts=models.CharField(max_length = 30,blank = True)
	contacts_phone=models.CharField(max_length = 11,blank = True)
	material_name=models.CharField(max_length = 50,blank = True)
	amount=models.CharField(max_length = 30,blank = True)
	price=models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 30,blank = True)
  	create_time = models.DateTimeField(auto_now_add = True, blank = True)
 	notes=models.CharField(max_length = 100,blank = True)
