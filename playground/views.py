from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from store.models import Product, Collection
from tags.models import TaggedItem

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    # collection = Collection(pk=1)
    # collection.delete()
    
    # OR
    
    Collection.objects.filter(id__gt=5).delete() # to delete multiple object
    
    return render(request,'hello.html',{'name':'Migbaru'})
