from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('auth/register/', views.register, name='register'),
]