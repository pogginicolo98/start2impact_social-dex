from api import views
from django.urls import path


urlpatterns = [
    path('posts', views.posts, name='posts_api'),
    path('new-post/', views.NewPost.as_view(), name='new_post'),
]
