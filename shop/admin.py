from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ["title", "description", "price"]


admin.site.register(Product, ProductAdmin)
