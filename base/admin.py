from django.contrib import admin
from .models import Customer, Product

# Register your models here.

admin.site.register(
    Customer
)
admin.site.register(Product)