from django.contrib import admin
from .models import Post, Author, Category, PostCategory, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author']


admin.site.register(Post)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)




