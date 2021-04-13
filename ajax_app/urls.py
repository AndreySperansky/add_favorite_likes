from django.urls import path
from .views import index_view, add_remove_like

app_name = 'ajax_app'

urlpatterns = [
    path('', index_view, name='index'),
    path('post/',  add_remove_like, name='like-post'),
]