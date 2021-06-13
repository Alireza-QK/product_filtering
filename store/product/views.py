from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Product, Category
from .forms import ProductCreateForm, CategoryCreateForm


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

			return redirect(reverse('product:product_create'))
		
	else:
		product_form = ProductCreateForm()

	context = {
		'form': product_form
	}

	return render(request, 'product/create.html', context)



# Show list category
def category_list(request):

	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, 'category/list.html', context)


# Create a category
def create_category(request):

	if request.method == 'POST':
		category_form = CategoryCreateForm(request.POST)

		if category_form.is_valid():
			title = category_form.cleaned_data.get('title')
			print(title)
			Category.objects.create(
				title=title,
				slug=slugify(title),
				created=timezone.now()
			)

			return redirect(reverse('product:category_create'))

	else:
		category_form = CategoryCreateForm()
	
	context = {
		'form': category_form,
		'title': 'Create new Category'
	}

	return render(request, 'category/create.html', context)


# Delete categoy
def category_delete(request, pk):

	category = get_object_or_404(Category, pk=pk)

	category.delete()
	messages.success(request, 'Delete successfuly.')
	return redirect(reverse('product:category_list'))

	return redirect(reverse('product:category_list'))


#update
def category_edit(request, pk):

	category = get_object_or_404(Category, pk=pk)

	if request.method == "POST":
		form = CategoryCreateForm(request.POST, instance=category)
		if form.is_valid():
			cd = form.cleaned_data
			category = form.save(commit=False)
			category.title = cd['title']
			category.slug = slugify(cd['title'])
			category.save()
			return redirect(reverse('product:category_list'))
	else:
		form = CategoryCreateForm(instance=category)
	return render(request, 'category/create.html', {'form': form, 'title': 'Edit category'})
