from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    title = models.CharField(verbose_name='title', max_length=255)
    slug = models.SlugField(verbose_name='slug', max_length=255, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.slug)
        
        super().save(*args, **kwargs)


class Product(models.Model):

    # Select a category for product
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', blank=True)

    title = models.CharField(verbose_name='title', max_length=255)
    slug = models.SlugField(verbose_name='Slug', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Price')
    description = models.TextField()
    image = models.ImageField(upload_to='product/images/', blank=True)

    count_stock = models.IntegerField(default=0)
    count_like = models.IntegerField(default=0)
    count_views = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.slug)
        
        super().save(*args, **kwargs)
    