from django.urls import path

from . import views

urlpatterns = [
    path('', views.profiles, name='users'),
    path('profile/<str:pk>/', views.profile, name='profile')

]
