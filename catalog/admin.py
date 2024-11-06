from django.contrib import admin
from .models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', )
    list_filter = ('category', )
    search_fields = ('name', 'category__name', 'description', 'category__description', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', )
    list_filter = ('name', 'email', )
    search_fields = ('name', 'email', 'message', )
