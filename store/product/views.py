from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Product, Category
from .forms import ProductCreateForm


def create_product(request):

	if request.method == 'POST':
		product_form = ProductCreateForm(request.POST, files=request.FILES)
		
		if product_form.is_valid():
			cd = product_form.cleaned_data
			
			Product.objects.create(
				title=cd['title'],
				slug=slugify(cd['title']),
				price=cd['price'],
				description=cd['description'],
				category=cd['category'],
				image=cd['image'],
				count_stock=cd['count_stock'],
				count_like=cd['count_like'],
				count_views=cd['count_views'],
			)
			messages.success(request, 'Product create successfuly.')

			return redirect(reverse('product:create'))
		
	else:
		product_form = ProductCreateForm()

	context = {
		'form': product_form
	}

	return render(request, 'product/create.html', context)
