from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view(),name='register-api'),
    path('login/', views.LoginAPIView.as_view(),name='login-api'),
    path('logout/', views.LogoutAPIView.as_view(),name='logout-api'),
    
]
