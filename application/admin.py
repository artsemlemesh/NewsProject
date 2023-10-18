from django.contrib import admin
from .models import Post, Author, Category, PostCategory, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author', 'rat']



def nullify_posts(modeladmin, request, queryset):
    queryset.update(comment='applied method: nullify_post ', rating=0)
nullify_posts.short_description = 'emprty comment, nullify rating'

class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta._get_fields()]
    actions = [nullify_posts]




class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'options', 'time_of_creation', 'title']
    list_filter = ['time_of_creation', 'title']
    search_fields = ['title']


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PostCategory._meta._get_fields()]
    list_filter = ['category']





admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)




