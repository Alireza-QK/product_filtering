from django.shortcuts import render
from .models import Product, Category
from .forms import ProductCreateForm


def create_product(request):

    if request.method == 'POST':
        product_form = ProductCreateForm(request.POST)
        pass
    else:
        product_form = ProductCreateForm()
    
    context = {
        'form': product_form
    }
    return render(request, 'product/create.html', context)
