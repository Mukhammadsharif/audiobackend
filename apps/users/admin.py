from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'first_name', 'last_name', 'verified_at', 'image')
    list_display = ('username', 'email', 'first_name', 'last_name', 'verified_at')
