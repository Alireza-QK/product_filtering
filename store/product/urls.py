from django.urls import path
from .views import (
    create_product,

    create_category,
    category_list,
    category_delete,
    category_edit
)

app_name = 'product'

urlpatterns = [
    path('create/', create_product, name='product_create'),

    # Category
    path('category/list/', category_list, name="category_list"),
    path('category/add/', create_category, name='category_create'),
    path('category/remove/<int:pk>/', category_delete, name='category_delete'),
    path('category/edit/<int:pk>/', category_edit, name='category_edit'),
    
]
