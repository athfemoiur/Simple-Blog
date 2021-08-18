from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from user.forms import CustomUserChangeForm
from user.models import User


@register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'avatar')}),
    )
    list_display = UserAdmin.list_display + ('date_of_birth', 'show_posts')

    def show_posts(self, obj):
        return mark_safe(f"<a href=/user/{obj.pk}/posts>Show Posts</a>")

    show_posts.short_description = 'posts'

