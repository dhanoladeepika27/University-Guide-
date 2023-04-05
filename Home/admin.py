from django.contrib import admin
from Home.models import PagePosts


# Register your models here.

@admin.register(PagePosts)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)
