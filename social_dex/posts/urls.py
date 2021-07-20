from django.urls import include, path
from posts.views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('api/', include('posts.api.urls')),
]
