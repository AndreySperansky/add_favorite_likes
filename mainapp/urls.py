from django.urls import path
from .views import index_view, favorite_project

app_name = 'mainapp'

urlpatterns = [
    path('', index_view, name='index'),
    path('<int:albom_id>/favorite_album/', favorite_project, name='favorite'),
]