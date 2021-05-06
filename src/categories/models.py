from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()

class ProviderCategoryModel(models.Model):
    url = models.CharField(max_length=100)
    category = models.ForeignKey('CategoryModel',
        on_delete=models.CASCADE)
    provider = models.ForeignKey('providers.ProviderModel', on_delete=models.CASCADE)