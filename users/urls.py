from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginForm, name="login"),
    path('logout/', views.logoutForm, name="logout"),
    path('update_user/', views.updateUser, name='updateUser'),
]