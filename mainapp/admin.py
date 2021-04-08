from django.contrib import admin
from .models import ProjectProfile

# Видоизменяем админку
class ProjectProfileAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'project_name', 'artist', 'is_favorite')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', )
    # какие поля будут участвовать в поиске
    search_fields = ('project_name', 'artist')


admin.site.register(ProjectProfile, ProjectProfileAdmin)


