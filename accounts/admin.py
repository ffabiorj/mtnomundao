from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserAdminForm

class UserAdmin(BaseUserAdmin):

    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('name', 'age', 'city', 'email', 'password1', 'password2', 'photo')
        }),

    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('email', 'photo')
        }),
        ('Informações Básicas', {
            'fields': ('name', 'age', 'city', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['name', 'email', 'age', 'city', 'photo', 'is_active', 'is_staff', 'date_joined']

admin.site.register(User, UserAdmin)