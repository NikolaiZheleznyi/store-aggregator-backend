from django.db import models

class CategoryModel(models.Model):
    name = models.CharField
    created = models.DateField

class ProviderCategoryModel(models.Model):
    url = models.CharField
    category = models.ForeignKey
    provider = models.ForeignKey