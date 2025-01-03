from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from users import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'), 
    path('users/', include('users.urls')),  # Incluye las URLs de la aplicación 'users'
    path('music/', include('music.urls')), 
    path('', lambda request: redirect('users:login')),  # Redirigir a la página de login
]


# Servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
