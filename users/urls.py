from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('minha-url/', views.congrats),
    path('sair/', views.logoutuser),
]