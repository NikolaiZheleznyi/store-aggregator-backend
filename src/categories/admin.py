from django.contrib import admin
from .models import CategoryModel, ProviderCategoryModel

admin.site.register(CategoryModel)
admin.site.register(ProviderCategoryModel)