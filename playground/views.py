from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from store.models import Product
from tags.models import TaggedItem

# def say_hello(request):
#     return HttpResponse('Hello World')


def say_hello(request):
    query_set = TaggedItem.objects.get_tags_for(Product, 1)
     
    
    return render(request,'hello.html',{'name':'Migbaru', 'result':list(query_set)})
