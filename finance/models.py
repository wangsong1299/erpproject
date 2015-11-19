from django.db import models

# Create your models here.
class Finance(models.Model):
	productID=models.CharField(max_length = 10)
	delivery_time=models.CharField(max_length = 50,blank = True)
	product_name=models.CharField(max_length = 50,blank = True)
	order_amount =models.CharField(max_length = 30,blank = True)
	delivery_amount =models.CharField(max_length = 30,blank = True)
	price=models.CharField(max_length = 30,blank = True)
	total_fee=models.CharField(max_length = 11,blank = True)
	notes=models.CharField(max_length = 15,blank = True)

