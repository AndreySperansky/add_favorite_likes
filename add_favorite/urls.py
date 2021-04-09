
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls', namespace='main')),
    path('ajax/', include('ajax.urls', namespace='ajax')),
    path('cv/', include('cv_app.urls', namespace='cv')),
]


if settings.DEBUG:      # т.е. если DEBUG = True
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
