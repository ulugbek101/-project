from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    
    path('project/<str:pk>/', views.project_detail, name='project_detail'),
    
    path('create-project/', views.create_project, name='project_create'),
    path('update-project/<str:pk>/', views.update_project, name='project_update'),
    path('update-delete/<str:pk>/', views.delete_project, name='project_delete'),
    
    
]
