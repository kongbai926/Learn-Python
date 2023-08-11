# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserTable(AbstractUser):

    age = models.IntegerField(blank=True)  # 用户年龄 blank设置为True，可以不填，默认使用none填充数据库
    sex = models.CharField(max_length=2, blank=True)  # 用户性别
