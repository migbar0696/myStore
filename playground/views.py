from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from store.models import Product, Collection
from tags.models import TaggedItem

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()
    
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()
    
    
    
    collection = Collection.objects.filter(pk=11).update(title='Games', featured_product_id = None)
     
    
    return render(request,'hello.html',{'name':'Migbaru'})
