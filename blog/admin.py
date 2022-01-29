from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'content', 'author', 'date_posted'
    )
admin.site.register(Post, PostAdmin)