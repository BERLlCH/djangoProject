from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views as mainViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('registration/', mainViews.register, name='register')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
