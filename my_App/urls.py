from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_home),
    path('login/', views.login),
    path('api/', views.api)
]