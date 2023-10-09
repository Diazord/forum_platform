from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),

    path('create-room/', views.createRoom, name='create-room'),
    path('edit-room/<str:pk>', views.updateRoom, name='edit-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

    path('delete-message/<str:pk>', views.deleteMessage, name='delete-message'),
    path('edit-user/', views.editUser, name='edit-user'),

    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
]
