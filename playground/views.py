from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Collection, Order, OrderItem, Customer
from django.db import transaction
from django.db.models import Q


# def say_hello(request):
#     return HttpResponse('Hello World')


# @transaction.atomic()     # This wrap the entire say hello function
def say_hello(request):
    Order.objects.filter(Q(pk=3007) | Q(pk=3008)).delete()
        
    return render(request,'hello.html',{'name':'Migbaru'})
