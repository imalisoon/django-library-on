from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    #list_display = []
    pass


admin.site.register(CustomUser, CustomUserAdmin)
