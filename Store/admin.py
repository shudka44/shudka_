# filepath: /c:/Users/Honor/Desktop/SHUDKA44/SHUDKA44/Store/admin.py
from django.contrib import admin
from .models import Product, Customer, Purchase, Payment

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Payment)