from accounts.views import signup_view
from django.urls import path

urlpatterns = [
    path('signup/', signup_view, name="signup_view"),
]
