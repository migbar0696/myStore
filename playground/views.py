from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Collection, Order, OrderItem, Customer
from django.db import transaction


# def say_hello(request):
#     return HttpResponse('Hello World')


# @transaction.atomic()     # This wrap the entire say hello function
def say_hello(request):
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
        
        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unitprice = 10
        item.save
    
    
    
    
    return render(request,'hello.html',{'name':'Migbaru'})
