from django.db import models
from django.core.validators import MinValueValidator

class ProductModel(models.Model):
    name = models.CharField
    category = models.ForeignKey
    created = models.DateField

class ProviderProductModel(models.Model):
    name = models.CharField
    price = models.IntegerField([MinValueValidator(0)])
    code = models.IntegerField([MinValueValidator(0)])
    product = models.ForeignKey
    provide = models.CharField
    created = models.DateField