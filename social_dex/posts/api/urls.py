from django.urls import path
from posts.api.views import new_post, posts

urlpatterns = [
    path('posts/', posts, name='post-list'),
    path('new-post/', new_post, name='new-post'),
]
