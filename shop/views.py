from django.contrib.auth import authenticate, login
from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *

from math import ceil
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# class PostsView(ListView):
#     model = Product
#     print(model) 
#     paginate_by = 10    
#     context_object_name = 'products'
#     template_name = 'shop/all.html'
#     ordering=['product_id']

def registeruser(request):
    if request.method == 'POST':
        print("POST")
        form=RegisterUser(request.POST)
        print(form.is_valid)
        if form.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            print(form.cleaned_data.get("username"))
            print(form.cleaned_data.get("password"))
            print(form.cleaned_data.get("email"))
            print(form)
            return redirect('about')


    return redirect('shop')

def loginuser(request):
    print(request)  
    if request.method == 'POST':
        email=request.POST.get('lemail')
        password=request.POST.get('lpassword')
        print(email,password)
        user=User.objects.get(email=email)
        print(user.username)
        user=authenticate(request,username=user.username,password= password)
        print(user)
        if user is not None:
            print('user')
            messages.add_message(request,messages.SUCCESS,"account exist")
            login(request,user)
            return redirect('shop')

    
    return redirect('shop')
        


def shop(request):
    rform=RegisterUser()
    earphone=Product.objects.filter(category="earphone")
    smartphone=Product.objects.filter(category="smartphone")
    clothing=Product.objects.filter(category="clothing")
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
    params={"products":temp,"slides":[earphone_slides,smartphone_slides,clothing_slides,infinite1],"num_pro":range(len(temp)),"iter":zip(temp,range(len(temp))),'form':rform}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html',{'request':request})


def contact(request):
    return render(request,'shop/contact.html')


def product(request,id):
    product=Product.objects.get(product_id=id)
    params={"product":product}
    return render(request,'shop/product.html',params)

def checkout(request):
    return render(request,'shop/checkout.html')
    
def tracker(request):
    """
    docstring
    """
    
    pass  

def all(request):
    smartphone=Product.objects.filter(category="smartphone")
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