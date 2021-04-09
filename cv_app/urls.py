from django.urls import path
from .views import index_view

app_name = 'cv_app'

urlpatterns = [
    path('', index_view, name='index'),
    # path('cv/<int:pk>/bookmark',  BookmarkView.as_view(), name='bookmark'),
]