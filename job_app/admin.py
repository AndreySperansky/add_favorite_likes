from django.contrib import admin
from .models import *

class JobAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'vacancy')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', )
    # какие поля будут участвовать в поиске
    search_fields = ('cv',)


class BookmarkJobAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'user', 'obj',)
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id','user', 'obj', )
    # какие поля будут участвовать в поиске
    search_fields = ('user', 'obj')


admin.site.register(Job, JobAdmin,)
admin.site.register(BookmarkJob, BookmarkJobAdmin)
