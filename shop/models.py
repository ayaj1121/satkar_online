from os import stat_result, times
from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import ModelBase
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.

def cart():
    return {
        "cart":{}
    }
    

class Customer(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    cart=models.JSONField(default=cart,blank=True,null=True)
    add1=models.JSONField(default=dict)
    add2=models.JSONField(default=dict,blank=True,null=True)




class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField( max_length=50,default='')
    category=models.CharField(max_length=50,default='')
    pub_date=models.DateField()
    img=models.ImageField(upload_to="image",default='')
    desc=models.CharField(max_length=500,default='')
    price=models.IntegerField(default=0)
    discounted_price=models.IntegerField(default=0)
    
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer=ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    total_amount=models.IntegerField(default=0)
    status=models.JSONField(default=dict,blank=True,null=True)
    address=models.JSONField(default=dict,blank=True,null=True)
    transac_id=models.CharField(max_length=50,default='')



class OrderItem(models.Model):
    order_item_id=models.AutoField(primary_key=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    sell_price=models.IntegerField(default=0)
    sell_discount_price=models.IntegerField(default=0)
