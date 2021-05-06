from django.contrib import admin
from .models import ProductModel, ProviderProductModel

class ProductModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProductModel, ProductModelAdmin)

class ProviderProductModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProviderProductModel, ProviderProductModelAdmin)