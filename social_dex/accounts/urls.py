from accounts.forms import CustomLoginForm, CustomPasswordChangeForm, CustomPasswordResetFrom, CustomSetPasswordForm
from accounts.views import signup_view
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('signup/', signup_view, name="signup_view"),
    path('login/', views.LoginView.as_view(form_class=CustomLoginForm), name='login'),
    path('password_change/', views.PasswordChangeView.as_view(form_class=CustomPasswordChangeForm), name='password_change'),
    path('password_reset/', views.PasswordResetView.as_view(form_class=CustomPasswordResetFrom), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(form_class=CustomSetPasswordForm), name='password_reset_confirm'),
]
