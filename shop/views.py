from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
from math import ceil


def shop(request):
    temp=Product.objects.all()
    slides=ceil(len(temp)/4)
    params={"products":temp,"slides":range(slides)}
    for i in range(len(temp)):
        print(temp[i].desc)

    return render(request,'shop/index.html',params)

