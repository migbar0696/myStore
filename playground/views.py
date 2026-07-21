from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product, OrderItem

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    query_set = Product.objects.filter(id__in =OrderItem.objects.values('product__id').distinct() ).order_by('title')

    
    
    
    return render(request,'hello.html',{'name':'Migbaru', 'products':list(query_set)})
