from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'title', 'author')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'author')
    # какие поля будут участвовать в поиске
    search_fields = ('title', 'author')


class LikeAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user', 'post', 'value')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id','user', 'post', 'value')
    # какие поля будут участвовать в поиске
    search_fields = ('user', 'post', 'value')


admin.site.register(Article, ArticleAdmin,)
admin.site.register(Like, LikeAdmin)
