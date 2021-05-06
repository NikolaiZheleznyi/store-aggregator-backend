from django.db import models
from django.core.validators import MinValueValidator

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('categories.CategoryModel', on_delete=models.CASCADE)
    created = models.DateTimeField()

class ProviderProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField([MinValueValidator(0)])
    code = models.IntegerField([MinValueValidator(0)])
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE)
    provide = models.CharField(max_length=100)
    created = models.DateTimeField()