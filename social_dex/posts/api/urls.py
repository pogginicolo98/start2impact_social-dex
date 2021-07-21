from django.urls import path
from posts.api.views import new_post, posts, PostLatestListAPIView

urlpatterns = [
    path('posts/', posts, name='post-list'),
    path('new-post/', new_post, name='new-post'),
    path('latest/', PostLatestListAPIView.as_view(), name='post-latest'),
]
