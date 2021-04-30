from django.contrib import admin
from .models import ProductModel, ProviderProductModel

admin.site.register(ProductModel)
admin.site.register(ProviderProductModel)