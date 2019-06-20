from django.urls import path
from . import views

urlpatterns = [
    path('list_files/', views.FiledataListAPIView.as_view(),name='list'),
    path('upload_files/', views.FiledataCreateAPIView.as_view(),name='upload'),
	path('update_files/<slug:filename>/',views.FiledataUpdateAPIView.as_view(),name='update'),
    path('delete_files/<slug:filename>/',views.FiledataDeleteAPIView.as_view(),name='delete'),
]
