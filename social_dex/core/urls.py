from django.urls import path
from core.views import UserDetailView, UserListView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
]
