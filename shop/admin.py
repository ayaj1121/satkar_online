from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','desc','pub_date','category','img']
    list_editable=['product_name','desc','pub_date','img','category']


admin.site.register(Product,ProductAdmin)