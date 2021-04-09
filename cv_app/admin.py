from django.contrib import admin
from .models import *

class CvAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'cv')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', )
    # какие поля будут участвовать в поиске
    search_fields = ('cv',)


class BookmarkCvAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user', 'obj',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id','user', 'obj', )
    # какие поля будут участвовать в поиске
    search_fields = ('user', 'obj')


admin.site.register(CV, CvAdmin,)
admin.site.register(BookmarkCV, BookmarkCvAdmin)
