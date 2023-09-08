from django.contrib import admin
from .models import Post, Reply


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    # filter_horizontal = ('likes',)
    # readonly_fields = ('likes_count',)
    
    def likes_count(self, obj):
        return obj.likes.count()


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'content', 'created_at')
    list_filter = ('post', 'content')
    search_fields = ('content',)