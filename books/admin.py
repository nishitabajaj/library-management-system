from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser, Book

# ✅ Custom Admin User
class AdminUserAdmin(UserAdmin):
    model = AdminUser
    list_display = ('email', 'is_staff', 'is_active')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    filter_horizontal = ()

admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(Book)