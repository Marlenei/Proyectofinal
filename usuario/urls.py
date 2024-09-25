from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from blog.urls import path

urlpatterns = [
        # path("registro", views.Usuario_created, name = "registro"),
        path("inicio", views.inicio, name="inicio"),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('', views.dashboard, name='dashboard'),


]