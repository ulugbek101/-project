from django.urls import path

from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),

    path('account/', views.account, name='account'),
    path('account-edit/', views.account_edit, name='account_edit'),

    path('registration/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
