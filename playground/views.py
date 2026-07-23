from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from store.models import Product, OrderItem, Order

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    # query_set = Product.objects.select_related('collection').prefetch_related('promotions').all()
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    

    
    
    
    return render(request,'hello.html',{'name':'Migbaru', 'orders':list(query_set)})
