"""
Registers the Category and File models with the Django admin site.

This allows the Category and File models to be managed through the admin interface.
"""

from django.contrib import admin

from .models import Category, File, Payment

# admin.py

admin.site.register(Category)
admin.site.register(File)
admin.site.register(Payment)

