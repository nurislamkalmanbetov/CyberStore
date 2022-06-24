from csv import list_dialects
from re import search
from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','id']
    prepopulated_fields = {"slug":('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'image',
        'category',
        'created',
        'updated',
        'is_active'
    ]

@admin.register(MyLinks)
class MyLinkAdmin(admin.ModelAdmin):
    list_display = ['facebook']
