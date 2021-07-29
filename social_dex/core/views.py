from core.mixins import StaffMixin
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class UserListView(StaffMixin, ListView):
    """
    User list view that display a list of all users and the amount of post created by each user.

    * Only staff users can view the user list.
    """

    model = User
    context_object_name = 'users'
    template_name = 'core/user_list.html'


class UserDetailView(DetailView):
    """
    User detail view that display user's profile information.
    """

    model = User
    context_object_name = 'user'
    template_name = 'core/user_detail.html'
