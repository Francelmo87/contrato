from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'cpf', 'registration', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {
            'fields': ('cpf', 'registration', 'phone')
        }),
    )
