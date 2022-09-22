from django.contrib import admin
from django.urls import path, include
from .views import HomeView, cerrarSesion
from edificios.urls import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/',cerrarSesion,name='salir'),
    path('edificios/',include('edificios.urls', namespace='edificios')),
    # path('propietarios/',include('propietarios.urls', namespace='propietarios')),
    # path('departamentos/',include('departamentos.urls', namespace='departamentos')),
        
]