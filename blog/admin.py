from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published', 'view_count']
    list_filter = ['title', 'created_at', 'is_published', 'view_count']