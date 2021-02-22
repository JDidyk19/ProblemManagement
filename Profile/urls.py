from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('~', views.Home.as_view(), name='home'),

    path('@<str:username>', views.ProfileView.as_view(), name = 'profile'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
]