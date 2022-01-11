"""Users admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from users.models import User


class CustomUserAdmin(UserAdmin):
    """User model admin."""
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password', 'first_name', 'last_name', 'id_type', 'id_number', 'profession', 'profile',)
        }),
    )
    list_display = ('email', 'username', 'password', 'first_name', 'last_name', 'id_type', 'id_number', 'profession', 'profile',)
    list_filter = ('created', 'modified')

admin.site.register(User, CustomUserAdmin)