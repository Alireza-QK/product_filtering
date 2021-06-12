from django.shortcuts import render
from .models import Product, Category


def create_product(request):

    if request.method == 'POST':
        pass
    
    context = {}
    return render(request, 'product/create.html', context)
