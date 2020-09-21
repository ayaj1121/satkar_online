from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product


def shop(request):
    temp=Product.objects.all()
    params={"products":temp,"len":range(len(temp))}
    for i in range(len(temp)):
        print(temp[i].desc)

    return render(request,'shop/index.html',params)