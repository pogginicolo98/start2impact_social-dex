from django.urls import path
from core.views import HomepageView, UserListView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('users/', UserListView.as_view(), name='user-list'),
]
