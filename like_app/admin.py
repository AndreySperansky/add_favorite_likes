from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'title', 'author',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'title',)
    # какие поля будут участвовать в поиске
    search_fields = ('title', 'author')


class LikeAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user', 'value',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id','user', 'value', )
    # какие поля будут участвовать в поиске
    search_fields = ('user', 'value')


admin.site.register(Post, PostAdmin,)
admin.site.register(Like, LikeAdmin)
