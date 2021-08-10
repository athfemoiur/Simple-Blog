from django.contrib import admin
from django.contrib.admin import register

from category.models import Category


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
