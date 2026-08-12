from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

# Register your models here.
from store.admin import ProductAdmin
from tags.models import TaggedItem
from store.models import Product

class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    extra = 1

class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)