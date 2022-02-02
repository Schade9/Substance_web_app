from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Reply

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'content', 'author', 'date_posted'
    )
admin.site.register(Post, PostAdmin)

class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'message', 'sender', 'post', 'reply_date'
    )
admin.site.register(Reply, ReplyAdmin)