from django import forms
from .models import Product, Category


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'image', 'count_stock', 'count_like', 'count_views')
        