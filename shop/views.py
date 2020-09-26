from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
from math import ceil
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

# class PostsView(ListView):
#     model = Product
#     print(model) 
#     paginate_by = 10    
#     context_object_name = 'products'
#     template_name = 'shop/all.html'
#     ordering=['product_id']



def shop(request):
    earphone=Product.objects.filter(desc="earphone")
    smartphone=Product.objects.filter(desc="smartphone")
    clothing=Product.objects.filter(desc="clothing")
    infinite=list([])
    infinite1=list([])
    for j in range(0,50):
        infinite.append(list(chain(smartphone)))
    for i in infinite:
        for j in i:
            infinite1.append(j)
    print(len(infinite1))
    temp=[earphone,smartphone,clothing,infinite1]
    earphone_slides=range(ceil(len(earphone)/6))
    smartphone_slides=range(ceil(len(smartphone)/6))
    clothing_slides=range(ceil(len(clothing)/6))
    infinite1=range(ceil(len(infinite1)/6))
    params={"products":temp,"slides":[earphone_slides,smartphone_slides,clothing_slides,infinite1],"num_pro":range(len(temp)),"iter":zip(temp,range(len(temp)))}
    return render(request,'shop/index.html',params)

def about(request):
    earphone=Product.objects.filter(desc="earphone")
    smartphone=Product.objects.filter(desc="smartphone")
    clothing=Product.objects.filter(desc="clothing")
    infinite=list([])
    infinite1=list([])
    for j in range(0,5000):
        infinite.append(list(chain(smartphone)))
    for i in infinite:
        for j in i:
            infinite1.append(j)
    print(len(infinite1))
    temp=[earphone,smartphone,clothing,infinite1]
    earphone_slides=range(ceil(len(earphone)/6))
    smartphone_slides=range(ceil(len(smartphone)/6))
    clothing_slides=range(ceil(len(clothing)/6))
    infinite1=range(ceil(len(infinite1)/6))
    params={"products":temp,"slides":[earphone_slides,smartphone_slides,clothing_slides,infinite1],"num_pro":range(len(temp)),"iter":zip(temp,range(len(temp)))}
    return render(request,'shop/index.html',params)

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

def all(request):
    smartphone=Product.objects.filter(desc="smartphone")
    infinite=list([])
    infinite1=list([])
    for j in range(0,5000):
        infinite.append(list(chain(smartphone)))
    for i in infinite:
        for j in i:
            infinite1.append(j)
    products=infinite1
    paginator = Paginator(products, 40)
    page_num = request.GET.get('page', 1)
    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    print("pro",products)
    return render(request, 'shop/all.html', {'products': products})