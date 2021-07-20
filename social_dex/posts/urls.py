from django.urls import include, path
from posts.views import HomepageView, PostsListView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('posts/', PostsListView.as_view(), name='post-list-view'),
    path('api/', include('posts.api.urls')),
]
