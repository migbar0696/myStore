from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from store.models import Product, Collection
from tags.models import TaggedItem

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    
    # collection = Collection.objects.create(title='Video Games', featured_product_id = 1)
     
    
    return render(request,'hello.html',{'name':'Migbaru'})
