from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from django.db.models import value,Q , F, Func
from django.db.models.functions import Concat
from django.http import HttpResponse
from store.models import Product, OrderItem, Order, Customer

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    # query_set = Product.objects.select_related('collection').prefetch_related('promotions').all()
    # query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    # result = Customer.objects.annotate(new_id=F('id') + 1)
    
    query_set = Customer.objects.annotate(
        full_name = Func(F('first_name'), value(' '), F('last_name'), function='CONCAT')
    )
    
    query_set = Customer.objects.annotate(
        full_name = Concat('first_name', value(' '), 'lastname')
    )

    
    
    
    return render(request,'hello.html',{'name':'Migbaru', 'result':list(query_set)})
