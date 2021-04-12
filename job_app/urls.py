from django.urls import path
from .views import index_view, add_remove_bookmark

app_name = 'job_app'

urlpatterns = [
    path('', index_view, name='index'),
    path('vacancy/<int:pk>/bookmark',  add_remove_bookmark, name='bookmark'),
]