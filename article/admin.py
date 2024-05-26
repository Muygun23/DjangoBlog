from django.contrib import admin
from .models import Article, Comment

admin.site.register(Comment)

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "created_date"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Article

