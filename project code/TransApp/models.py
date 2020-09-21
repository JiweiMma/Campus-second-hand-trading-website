from django.db import models
class user(models.Model):
    name = models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class shoppingcart(models.Model):
    user_num=models.CharField(max_length=20)
    sell_num=models.CharField(max_length=20)
class sellbag(models.Model):
    user_num = models.CharField(max_length=20)
    sell_num = models.CharField(max_length=20)
class sell(models.Model):
    description=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
# Create your models here.
