from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post_confirmation, name='delete_post_confirmation'),
    path('post/<int:post_id>/delete/confirm/', views.delete_post, name='delete_post'),
]
