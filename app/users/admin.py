from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('emailUser', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('emailUser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('emailUser', 'passwordUser')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('emailUser', 'firstNameUser', 'passwordUser', 'password', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('emailUser',)
    ordering = ('emailUser',)


admin.site.register(CustomUser, CustomUserAdmin)