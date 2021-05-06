from django.contrib import admin
from .models import CategoryModel, ProviderCategoryModel

class CategoryModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(CategoryModel, CategoryModelAdmin)

class ProviderCategoryModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProviderCategoryModel, ProviderCategoryModelAdmin)