from django.urls import path
from core.views import UserDetailView, UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
