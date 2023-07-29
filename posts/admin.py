from django.contrib import admin

# Register your models here.
from .models import (
    Category,
    SubCategory,
    Post,
    Comment
)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    serach_fields = ['name']


@admin.register(SubCategory)
class AdminSubCategory(admin.ModelAdmin):
    list_display = ['category','name']
    list_filter = ['category']


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['author', 'writer', 'subcategory', "title", 'createdAt', 'updatedAt']
    list_filter = ["writer", 'createdAt', 'updatedAt']
    serach_fields = ['writer', 'title']
    prepopulated_fields = {"slug": ['title',]}



@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['post','createdAt', "user"]
    list_filter = ['post']
