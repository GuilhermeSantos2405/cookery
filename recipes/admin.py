from django.contrib import admin

from .models import Category, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at',
                    'updated_at', 'author', 'category', 'is_published']
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
