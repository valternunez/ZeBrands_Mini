#
# Add to Django Admin the models
#
from django.contrib import admin
from .models import Product, Brand

# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)