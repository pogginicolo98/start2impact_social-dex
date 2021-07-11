from api.views import PostListCreateAPIView
from django.urls import path


urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
]
