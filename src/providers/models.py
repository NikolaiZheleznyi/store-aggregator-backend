from django.db import models

class ProviderModel(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField()


