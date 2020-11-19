from django.contrib import admin
from .models import Newsletter, Blog

class NewsAdmin(admin.ModelAdmin):
    list_display=['email', 'time']
admin.site.register(Newsletter, NewsAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','time']
    search_fields=['title', 'content']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Blog, BlogAdmin)