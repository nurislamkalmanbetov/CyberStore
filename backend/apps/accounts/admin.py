from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'middle_name',
        'phone',
        'avatar'
    ]
