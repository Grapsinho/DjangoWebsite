from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room_page/<str:room_id>/', views.room, name="room"),
    path('room_create/', views.roomPage, name='roomCreate'),
    path('update_room/<str:pk>/', views.updateRoom, name='updateRoom'),
    path('delete_room/<str:pk>/', views.deleteRoom, name='deleteRoom'),
    path('delete_messages/<str:pk>/', views.deleteMessages, name='deleteMessages'),
    path('profile/<str:pk>/', views.userProfile, name='userProfile'),
]