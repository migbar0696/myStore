from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product, OrderItem

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    query_set = Product.objects.select_related('collection').prefetch_related('promotions').all()

    
    
    
    return render(request,'hello.html',{'name':'Migbaru', 'products':list(query_set)})
