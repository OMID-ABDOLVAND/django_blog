from django.contrib import admin
from .models import Category, Post, Comment


# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'publish_time', 'status']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body', 'lead',)
    list_filter = ('status', 'publish_time',)
    date_hierarchy = 'publish_time'
    raw_id_fields = ('author',)


admin.site.register(Comment)
