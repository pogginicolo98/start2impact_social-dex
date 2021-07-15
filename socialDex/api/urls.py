from api.views import new_post, posts
from django.urls import path

urlpatterns = [
    path('posts/', posts, name='post-list'),
    path('new-post/', new_post, name='new-post'),
]
