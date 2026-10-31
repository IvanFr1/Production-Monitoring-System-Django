from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from unfold.forms import (
    AdminPasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = (
        "username",
        "first_name",
        "last_name",
        "position",
        "email",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "position",
        "email",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительная информация", {"fields": ("position",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительная информация", {"fields": ("position",)}),
    )
