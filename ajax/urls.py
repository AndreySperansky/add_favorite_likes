from django.urls import path
from .__views import index_view, favorites_edit

app_name = 'ajax'

urlpatterns = [
    path('', index_view, name='index'),
    path('article/<int:pk>/bookmark',  favorites_edit, name='bookmark'),
]