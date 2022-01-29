from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'image'
    )
admin.site.register(Profile, ProfileAdmin)