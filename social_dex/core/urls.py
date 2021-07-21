from django.urls import path
from core.views import HomepageView, UserDetailView, UserListView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
]
