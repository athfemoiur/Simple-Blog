from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from user.forms import CustomUserChangeForm
from user.models import User


@register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'avatar')}),
    )
    list_display = UserAdmin.list_display + ('date_of_birth',)
