from django.contrib import admin
from django.contrib.admin import register

from comment.models import Comment
from post.models import Post


class LikeInline(admin.TabularInline):
    can_delete = False
    verbose_name = 'Like'
    verbose_name_plural = 'Likes'
    model = Post.likes.through
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CommentInline(admin.TabularInline):
    can_delete = False
    verbose_name = 'Comment'
    verbose_name_plural = 'Comments'
    model = Comment
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('likes',)
    list_display = ('title', 'author', 'status', 'slug', 'like_count')
    list_editable = ('status',)
    list_filter = ('status', 'categories')
    search_fields = ('title', 'author__username', 'categories__name')
    actions = ('draft_all_posts',)
    inlines = [CommentInline, LikeInline]

    @admin.action(description='Make all posts, draft')
    def draft_all_posts(self, request, queryset):
        queryset.update(status=Post.DRAFT)
