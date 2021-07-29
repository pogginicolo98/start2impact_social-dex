from django.urls import path
from posts.api.views import LatestPostListAPIView, new_post, posts

urlpatterns = [
    path('posts/', posts, name='post-list'),
    path('new-post/', new_post, name='new-post'),
    path('posts/latest/', LatestPostListAPIView.as_view(), name='post-latest'),
]
