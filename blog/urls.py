from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/delete/confirm/', views.delete_post_confirmation, name='delete_post_confirmation'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]