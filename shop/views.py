import json
from django.contrib.auth import authenticate, login,logout  
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pytz import timezone
# Create your views here.
from .models import *
from .forms import *

import pytz
import datetime
from math import ceil, log
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from shop.paytm.checksum import generateSignature, verifySignature

import sys

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
        if form.is_valid():
            if User.objects.get(email=form.cleaned_data.get("email")):
                messages.add_message(request,messages.ERROR,"User Exist")
                return redirect('shop')
            else:    
                user=form.save()
                user.set_password(form.cleaned_data.get("password"))
                user.save()
                Customer.objects.create(user=user,phone=request.POST['phone'])
                print(form.cleaned_data.get("username"))
                print(form.cleaned_data.get("password"))
                print(form.cleaned_data.get("email"))
                print(form)
                return redirect('shop')
        else:
            messages.add_message(request,messages.ERROR,"User Exist")
            return redirect('shop')





def loginuser(request):
    print(request)  
    if request.method == 'POST':
        email=request.POST.get('lemail')
        password=request.POST.get('lpassword')
        print(email,password)
        try:
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            user=None
        if user is not None:
            user=authenticate(request,username=user.username,password= password)
            print(user)
            messages.add_message(request,messages.SUCCESS,"account loggedin")
            login(request,user)
        else:
            messages.error(request,"Uer doesnot exist please Signup !")

    return redirect('shop')
        
@login_required(login_url='shop')
def logoutuser(request):
    print(json.loads(request.POST.get("cart")))
    customer=Customer.objects.get(user=request.user.id)
    customer.cart["cart"]=json.loads(request.POST["cart"])
    customer.save()
    logout(request)
    return redirect('shop')

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
    
def orders(request):
    return render(request,'shop/orders.html')

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

@login_required(login_url='shop')
def placeorder(request):
    if request.method == 'POST':
        address={}
        address['fname']=request.POST['firstname']
        print('fname',request.POST['firstname'])
        address['email']=request.POST['email']
        print('email',request.POST['email'])
        address['address']=request.POST['address']
        address['city']=request.POST['city']
        address['phone']=request.POST['phone']
        address['state']=request.POST['state']
        address['zipcode']=request.POST['zip']
        print("address",address)
        user=Customer(user=request.user)
        orderitems=json.loads(request.POST['orderitems'])
        for i in orderitems:
            print(i)
        order=Order(customer=user,total_amount=orderitems[3]["totalamount"],address=address,orderitems=orderitems)
        order.save()
        data_dict = {
            'MID':'DSJzTF95702911495385',
            'ORDER_ID':str(order.order_id),
            'TXN_AMOUNT':str(orderitems[3]["totalamount"]),
            'CUST_ID':str(request.user.id),
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        data_dict["CHECKSUMHASH"]=generateSignature(data_dict,'hHzOo8wUm&hizMaJ')
        return render(request,'shop/paytm.html',{'data_dict':data_dict})

    return redirect('checkout')

@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    status={}
    for i in form.keys():
        response_dict[i]=form[i]
        if i == 'CHECKSUMHASH':
            checksum=form[i]
    verify=verifySignature(response_dict,'hHzOo8wUm&hizMaJ',checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successfully')
            status[datetime.datetime.utcnow().strftime("%c")]="orderplaced"
            orders=Order.objects.get(order_id=response_dict['ORDERID'])
            orders.res_msg=response_dict
            orders.last_status_code=0
            orders.status=status
            orders.save()
    return HttpResponse('done')
