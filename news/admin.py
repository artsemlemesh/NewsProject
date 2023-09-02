from django.contrib import admin
from .models import NewsCategory, News


admin.site.register(NewsCategory)
admin.site.register(News)
