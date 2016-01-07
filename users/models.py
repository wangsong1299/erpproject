#! -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
    
    UNKNOWN = 0
    MEAL = 1
    FEMEAL = 2
    SEXY_CHOICES = (
            (UNKNOWN, '保密'),
            (MEAL, '男'),
            (FEMEAL, '女'),
    )
    phone = models.CharField(max_length = 12, unique = True)
    nick_name = models.CharField(max_length = 20, unique = True)
    signin_passwd = models.CharField(max_length = 128)
    sexy = models.IntegerField(default = UNKNOWN,
                                choices = SEXY_CHOICES)
    qq = models.CharField(max_length = 12)
    role = models.IntegerField(max_length = 2)
    p1 = models.CharField(default = 0,max_length=1)
    p2 = models.CharField(default = 0,max_length=1)
    p3 = models.CharField(default = 0,max_length=1)
    p4 = models.CharField(default = 0,max_length=1)
    p5 = models.CharField(default = 0,max_length=1)
    p6 = models.CharField(default = 0,max_length=1)
    p7 = models.CharField(default = 0,max_length=1)
    p8 = models.CharField(default = 0,max_length=1)
    p9 = models.CharField(default = 0,max_length=1)
    p10 = models.CharField(default = 0,max_length=1)

