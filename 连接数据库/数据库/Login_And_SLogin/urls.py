from django.urls import path

from . import tests, views

urlpatterns = {
    path('', views.Login_Slogin),
    path('login/', views.auth_Login, name='login'),
    path('register/', views.auth_Register, name='register'),
    path('logout/', views.auth_LogOUT, name='logOUT'),
    path('get/', tests.get_test, name='get_test'),
    }
