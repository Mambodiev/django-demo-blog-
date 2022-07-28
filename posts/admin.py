from django.contrib import admin
from .models import ( Post, PostView, Comment, Like, User
)


class PostAdmin(admin.ModelAdmin):
    list_display = [
                    'title', 
                    'author', 
                    'slug'
                    ]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(User)