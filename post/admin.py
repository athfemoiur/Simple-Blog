from django.contrib import admin
from django.contrib.admin import register

from post.models import Post


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'slug')
    list_editable = ('status',)
    list_filter = ('status', 'categories')
    search_fields = ('title', 'author__username', 'categories__name')
    actions = ('draft_all_posts',)

    @admin.action(description='Make all posts, draft')
    def draft_all_posts(self, request, queryset):
        queryset.update(status=Post.DRAFT)
