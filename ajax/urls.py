from django.urls import path
from .views import index_view, BookmarkView

app_name = 'ajax'

urlpatterns = [
    path('', index_view, name='index'),
    path('article/<int:pk>/bookmark',  BookmarkView.as_view(), name='bookmark'),
]