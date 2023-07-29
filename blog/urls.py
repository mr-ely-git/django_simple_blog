from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-url'),
    path('posts', views.posts, name='all-posts-url'),
    path('posts/<slug:slug>', views.single_post, name='single-post-url')
]
