from django import forms
from .models import Product, Category


class ProductCreateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
	
	class Meta:
		model = Product
		fields = ('title', 'price', 'description', 'category', 'image', 'count_stock', 'count_like', 'count_views')
	
	def clean_price(self):
		price = self.cleaned_data.get('price')

		if price is None or price < 0:
			price = 0
			raise forms.ValidationError('Please enter a price valid')
		
		return price

	def clean_count_stock(self):
		count_stock = self.cleaned_data.get('count_stock')

		if count_stock is None or count_stock < 0:
			count_stock = 0
			raise forms.ValidationError('Please enter a count stock valid')
		
		return count_stock

	def clean_count_like(self):
		count_like = self.cleaned_data.get('count_like')

		if count_like is None or count_like < 0:
			count_like = 0
			raise forms.ValidationError('Please enter a count like valid')
		
		return count_like

	def clean_count_views(self):
		count_views = self.cleaned_data.get('count_views')

		if count_views is None or count_views < 0:
			count_views = 0
			raise forms.ValidationError('Please enter a count views valid')
		
		return count_views


class CategoryCreateForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ('title', )

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name...'})
		}
