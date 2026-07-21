from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    query_set = Product.objects.filter(last_update__year = 2021)
    

    return render(request,'hello.html',{'name':'Migbaru', 'products':list(query_set)})
