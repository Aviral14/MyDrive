from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('view_files/', views.view),
    path('upload_files/', views.upload),
   # path('upload/delete_files/', views.delete),
    #path('search_files/', views.search),
]
