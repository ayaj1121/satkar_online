"""satkar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib.auth import login
from .models import Product
from django.db import models

from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.shop,name="shop"),
    path('about/',views.about,name='about'),
    path('checkout/',views.checkout,name='checkout'),
    path("all/", views.all, name="all"),
    path("contact/", views.contact, name="contact"),
    path("orders/", views.orders, name="orders"),
    path("checkout/placeorder/", views.placeorder, name="placeorder"),
    path("handlerequest/", views.handlerequest, name="handlerequest"),




    path('login/',views.loginuser,name='login'),
    path('register/',views.registeruser,name='register'),
    path('logout/',views.logoutuser,name='logout'),



    
    path('product/<int:id>',views.product),
    path('all/product/<int:id>',views.product),
    path('checkout/product/<int:id>',views.product),


]
