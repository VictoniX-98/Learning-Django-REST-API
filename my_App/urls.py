from django.urls import path
from .models import views

urlpatterns = [
    path('login/', views.login)
]