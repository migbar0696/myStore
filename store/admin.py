from django.contrib import admin, messages
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

from . import models

# Register your models here.

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [
            ('<10','Low'),
            ('high', 'High')
        ]
        
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt = 10)
        elif self.value() == 'high':
            return queryset.filter(inventory__gte = 10)
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title', 'inventory']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update',InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    
    def collection_title(self, product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    @admin.action(description='clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} products updated successfully',
            messages.SUCCESS
        )
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    
    def order_count(self, customer):
        url = (reverse('admin:store_order_changelist')
             + '?'
             + urlencode(
                 {
                     'customer__id' :customer.id
                 }
             )
               )
        return format_html('<a href = {}>{}</a>', url, customer.order_quantity)
    


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_quantity = Count('order')
        )
    
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer' ]



    
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    
    @admin.display(ordering='products_quantity')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
              + "?"
              + urlencode(
                  {
                     'collection__id':str(collection.id)
                  }
                  
              )
               )
        return format_html('<a href="{}">{}</a>',url,  collection.products_quantity)
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_quantity = Count('product')
        )
    
    
    


