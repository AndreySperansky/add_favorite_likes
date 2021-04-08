from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'title')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', )
    # какие поля будут участвовать в поиске
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin,)
# admin.site.register(BookmarkArticle,)
