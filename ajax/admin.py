from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'title')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', )
    # какие поля будут участвовать в поиске
    search_fields = ('title',)


class BookmarkArticleAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user', 'obj',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id','user', 'obj', )
    # какие поля будут участвовать в поиске
    search_fields = ('user', 'obj')


admin.site.register(Article, ArticleAdmin,)
admin.site.register(BookmarkArticle, BookmarkArticleAdmin)
