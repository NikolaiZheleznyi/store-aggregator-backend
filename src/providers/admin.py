from django.contrib import admin
from .models import ProviderModel

class ProviderModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProviderModel, ProviderModelAdmin)
