from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
from math import ceil


def shop(request):
    earphone=Product.objects.filter(desc="earphone")
    smartphone=Product.objects.filter(desc="smartphone")
    clothing=Product.objects.filter(desc="clothing")
    temp=[earphone,smartphone,clothing]
    earphone_slides=range(ceil(len(earphone)/6))
    smartphone_slides=range(ceil(len(smartphone)/6))
    clothing_slides=range(ceil(len(clothing)/6))
    params={"products":[earphone,smartphone,clothing],"slides":[earphone_slides,smartphone_slides,clothing_slides],"num_pro":range(len(temp)),"iter":zip(temp,range(len(temp)))}
    return render(request,'shop/index.html',params)

def about(request):
    """
    docstring
    """
    return render(request,'shop/about.html')

def product(request):
    """
    docstring
    """
    pass

def checkout(request):
    """
    docstring
    """
    pass

def tracker(request):
    """
    docstring
    """
    pass    