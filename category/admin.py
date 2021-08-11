from django.contrib import admin
from django.contrib.admin import register
from category.models import Category
from post.models import Post


class CategoryProductsInline(admin.TabularInline):
    model = Post.categories.through
    can_delete = False
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
    extra = 0


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [CategoryProductsInline]
