"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]

# Development ve production'da media files serve etmek için
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Production için media files ayarı
if not settings.DEBUG:
    # Production'da media files için
    settings.MEDIA_URL = '/media/'
    settings.MEDIA_ROOT = settings.BASE_DIR / 'media'
    
    # CSRF ayarları da buraya ekleyelim
    settings.CSRF_COOKIE_SECURE = True
    settings.CSRF_COOKIE_SAMESITE = 'Lax'
    settings.SESSION_COOKIE_SECURE = True
else:
    # Development ayarları
    settings.MEDIA_URL = '/media/'
    settings.MEDIA_ROOT = settings.BASE_DIR / 'media'
