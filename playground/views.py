from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    # query_set = Product.objects.values('id', 'title', 'collection__title')
    query_set = Product.objects.values_list('id', 'title', 'collection__title')
    
    
    
    
    return render(request,'hello.html',{'name':'Migbaru', 'products':list(query_set)})
