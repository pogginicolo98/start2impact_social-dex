from django.urls import include, path
from posts.views import PostListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('api/', include('posts.api.urls')),
]
