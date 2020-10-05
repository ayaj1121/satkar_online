from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','desc','pub_date','category','img','price','discounted_price']
    list_editable=['product_name','desc','price','discounted_price','img','category']

class OrderAdmin(admin.ModelAdmin):
    list_display=['order_id','customer','date','time','total_amount','status','address','transac_id']
    list_editable=['customer','total_amount']
    # list_display_links = None

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order_item_id','order','product','quantity','sell_price','sell_discount_price']
    list_editable=['order','product','quantity','sell_price','sell_discount_price']
    # list_display_links = None

class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','phone','add1','add2','cart']
    list_display_links = ['user']
    list_editable=['phone','add1','add2','cart']


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Customer,CustomerAdmin)
