from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models import Q , F, Func, ExpressionWrapper, DecimalField, Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from store.models import Product, OrderItem, Order, Customer

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    discount_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    query_set = Product.objects.annotate(
        discount_price = discount_price
    )
     
    
    return render(request,'hello.html',{'name':'Migbaru', 'result':list(query_set)})
