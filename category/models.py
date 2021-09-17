from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name =models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    # class Meta:                                             ## as default django takes as plural like categories wil become 
    #     verbose_name = 'category'                           ##  categorys automatically so to make it categories we have to 
    #     verbose_name_plural = 'categories'                  ##  do change in class meta
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
        
    def __str__(self):
        return self.category_name