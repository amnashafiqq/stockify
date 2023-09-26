from django.contrib import admin
from store.models.products import Products
from store.models.category import Category
from store.models.customer import Customer
from store.models.order import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'status', 'date']
    list_filter = ['status', 'date']  
    search_fields = ["customer"]
    class Media:
        css = {
            'all': ('store/css/admin_custom.css',),  # Path to your custom CSS file
        }

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order,OrderAdmin)

