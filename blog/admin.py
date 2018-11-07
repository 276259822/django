from django.contrib import admin
from .models import Category, Tag, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_time')
    ordering = ['-created_time']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_time')
    ordering = ['-created_time']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    ordering = ['-created_time']
