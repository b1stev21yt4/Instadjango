from django.contrib import admin
from django.urls import path, include

from Insta.views import (HelloDjango, PostsView, PostDetailView, 
                         PostCreateView, PostUpdateView, PostDeleteView, 
                         addLike, UserDetailView)

urlpatterns = [
    path('hellodjango', HelloDjango.as_view(), name='hellodjango'),
    path('', PostsView.as_view(), name = 'posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('posts/new/', PostCreateView.as_view(), name = 'make_post'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name = 'post_update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),    
]