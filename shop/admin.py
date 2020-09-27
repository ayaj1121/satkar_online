from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','desc','pub_date','category','img','price','discounted_price']
    list_editable=['product_name','desc','price','discounted_price','img','category']


admin.site.register(Product,ProductAdmin)