from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'category', 'count_stock', 'count_like', 'count_views', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'created')
