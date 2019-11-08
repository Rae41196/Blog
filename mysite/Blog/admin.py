from django.contrib import admin
from .models import Post

#Register models here to have ability to create posts from the admin panel.
class PostAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'blog_slug': ('blog_title',)}


admin.site.register(Post, PostAdmin)