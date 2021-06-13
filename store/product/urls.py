from django.urls import path
from .views import (
    product_list,
    create_product,
    product_edit,
    product_delete,

    # Product home
    homePage,

    create_category,
    category_list,
    category_delete,
    category_edit,
)

app_name = 'product'

urlpatterns = [
    path('list/', product_list, name="product_list"),
    path('create/', create_product, name='product_create'),
    path('edit/<int:pk>/', product_edit, name="product_edit"),
    path('remove/<int:pk>/', product_delete, name="product_delete"),

    # Product home
    path('', homePage, name="home"),

    # Category
    path('category/list/', category_list, name="category_list"),
    path('category/add/', create_category, name='category_create'),
    path('category/remove/<int:pk>/', category_delete, name='category_delete'),
    path('category/edit/<int:pk>/', category_edit, name='category_edit'),
    
]
