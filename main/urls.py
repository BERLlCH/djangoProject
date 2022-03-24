from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', views.index, name='main'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('exit', LogoutView.as_view(template_name='main/index.html'), name='exit'),
    path('login/main', views.index),
    path('ads', views.ads, name='ads'),
    path('newAd', views.newad, name='newad'),
    path('myAds', views.myads, name='myads')
]