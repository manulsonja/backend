from django.contrib import admin
from .models import BlogArticle, Image, ContentChunk

class PhotoAdmin(admin.StackedInline):
    model = Image
    extra = 1

class ContentChunkAdmin(admin.StackedInline):
    model = ContentChunk
    extra = 1

# Register your models here.
class BlogArticleAdmin(admin.ModelAdmin):
    model = BlogArticle
    inlines = [ContentChunkAdmin, PhotoAdmin]


admin.site.register(BlogArticle, BlogArticleAdmin)