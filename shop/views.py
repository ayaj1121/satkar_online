import json
from django.contrib.auth import authenticate, login,logout  
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *

from math import ceil, log
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

def getdata(request):
    print(request.POST["cart"])
    return JsonResponse({'status':'save'})

def auth(request):
    if request.user.is_authenticated:
        print(request.user.id)
        return Customer.objects.get(user=request.user.id)
    else:
        return None

def cartcall(request):
    userid=auth(request)
    if userid is not None:    
        customer=Customer.objects.get(user=userid)
        print(customer.cart)
        cartid=customer.cart["cart"]
        print("cartid",cartid)
        cartitem={}
        cartitemprice={}
        for c in cartid:
            product=Product.objects.get(product_id=c)
            cartitem[c]=product.product_name
            cartitemprice[c]=product.price
        return json.dumps({'cartitem':cartitem,'cartitemprice':cartitemprice,'cart':cartid})
    return json.dumps({'cartitem':{},'cartitemprice':{},'cart':{}})

def registeruser(request):
    if request.method == 'POST':
        form=RegisterUser(request.POST)
        print(form.is_valid)
        if not form.is_valid() and User.objects.get(email=form.cleaned_data.get("email")):
            messages.add_message(request,messages.ERROR,"User Exist")
            return redirect('shop')
        else:    
            user=form.save()
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            print(form.cleaned_data.get("username"))
            print(form.cleaned_data.get("password"))
            print(form.cleaned_data.get("email"))
            print(form)
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
            messages.add_message(request,messages.SUCCESS,"account loggedin")
            login(request,user)
            return redirect('shop')

    
    return redirect('shop')
        
@login_required(login_url='shop')
def logoutuser(request):
    print(request.POST["temp"])
    print(request.POST["cart"])
    customer=Customer.objects.get(user=request.user.id)
    customer.cart["cart"]=json.loads(request.POST["cart"])
    customer.save()
    logout(request)
    return JsonResponse({"status":"success"})

def shop(request):
    rform=RegisterUser()
    cart=cartcall(request)
    print("cart",cart)
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
    params={"products":temp,"slides":[earphone_slides,smartphone_slides,clothing_slides,infinite1],"num_pro":range(len(temp))
    ,"iter":zip(temp,range(len(temp))),'form':rform,'cart':cart}
    return render(request,'shop/index.html',params)

def about(request):
    user=User.objects.get(id=1)
    print(user)
    param=Customer.objects.get(user=user)
    print(param.add1["country"])
    return render(request,'shop/about.html',{'request':request,"param":param})


def contact(request):
    return render(request,'shop/contact.html')


def product(request,id):
    product=Product.objects.get(product_id=id)
    params={"product":product}
    return render(request,'shop/product.html',params)

@login_required(login_url='shop')
def checkout(request):
    return render(request,'shop/checkout.html')
    
def tracker(request):

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