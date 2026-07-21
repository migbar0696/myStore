from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from store.models import Product

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    # query_set = Product.objects.filter(unit_price__lt = 20, inventory__lt = 10)
    # query_set = Product.objects.filter(unit_price__lt = 20).filter(inventory__lt = 10)
    query_set = Product.objects.filter(Q(unit_price__lt = 20) | ~Q(inventory__lt=10))
    
    
    return render(request,'hello.html',{'name':'Migbaru', 'products':list(query_set)})
