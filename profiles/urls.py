from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('get_friends/', views.get_friends, name='get_friends'),
    path('send_friend_request/<int:friend_id>/', views.send_friend_request, name='send_friend_request'),
    path('determine_friend_email/<int:friend_id>/', views.determine_friend_email, name='determine_friend_email'),
]
