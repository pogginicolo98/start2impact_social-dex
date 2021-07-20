from django.urls import include, path
from posts.views import HomepageView, PostListCreateView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/', include('posts.api.urls')),
]
