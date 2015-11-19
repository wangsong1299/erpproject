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

    administrator = 0
    boss = 1
    manager = 2
    worker = 3
    ROLE_CHOICES = (
            (administrator, '系统管理员'),
            (boss, '公司领导'),
            (manager, '部门经理'),
            (worker, '操作员'),
    )

    sales = 0
    management = 1
    finance = 2
    work = 3
    DEPARTMENT_CHOICES = (
            (sales, '销售部'),
            (management, '管理部'),
            (finance, '财务部'),
            (work, '生产部'),
    )


    phone = models.CharField(max_length = 12, unique = True)
    nick_name = models.CharField(max_length = 20, unique = True)
    signin_passwd = models.CharField(max_length = 128)
    sexy = models.IntegerField(default = UNKNOWN,
                                choices = SEXY_CHOICES)
    qq = models.CharField(max_length = 12)
    role = models.IntegerField(default = worker,
                                choices = ROLE_CHOICES)
    department = models.IntegerField(default = work,
                                choices = DEPARTMENT_CHOICES)
    permission = models.CharField(max_length = 30)

