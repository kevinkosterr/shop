from django.contrib import admin
from .models import Product

from users.models import ShopUser


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ["username", "email", "password"]


class ProductAdmin(admin.ModelAdmin):
    fields = ["title", "description", "price"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ShopUser, UserAdmin)
