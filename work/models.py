from django.db import models

# Create your models here.
class Tracking(models.Model):
	productID=models.CharField(max_length = 10)
	product_name=models.CharField(max_length = 50,blank = True)
	customer =models.CharField(max_length = 30,blank = True)
	state =models.CharField(max_length = 2,default=0)
	pipline_step=models.CharField(max_length = 4,default=0)
	create_time=models.CharField(max_length = 30,blank = True)
	deadline=models.CharField(max_length = 11,blank = True)
	notes=models.CharField(max_length = 30,blank = True)

class Worker(models.Model):
	workerID =models.CharField(max_length = 30)
	worker_name=models.CharField(max_length = 30)
	productID=models.CharField(max_length = 30)
	product_name=models.CharField(max_length = 30,blank=True)
	pipline_step=models.CharField(max_length = 4,default=0)
	count=models.CharField(max_length = 30,default=0)
	salary=models.CharField(max_length = 30,default=0)
	create_time = models.DateTimeField(auto_now_add = True, blank = True)
	notes=models.CharField(max_length = 30,blank=True)
