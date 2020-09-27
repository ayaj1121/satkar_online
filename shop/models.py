from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField( max_length=50,default='')
    category=models.CharField(max_length=50,default='')
    pub_date=models.DateField()
    img=models.ImageField(upload_to="image",default='')
    desc=models.CharField(max_length=500,default='')
    price=models.IntegerField(default=0)
    


    