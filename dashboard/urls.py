from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('posts',views.posts,name="posts"),
    path('posts/<str:post_id>',views.post,name="post"),
    path('like/<str:post_id>',views.like,name="like"),
    path('comment/<str:post_id>',views.comment,name="comment"),
    path('create-post',views.create_post,name="create-post"),
    path('profile',views.profile,name="profile"),
    path('change-password',views.change_password,name="change-password"),
]
