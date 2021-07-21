from core.mixins import StaffMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.list import ListView


class HomepageView(TemplateView):
    """
    Temporary homepage
    """

    template_name = 'core/homepage.html'


class UserListView(StaffMixin, ListView):
    """
    User view to list all users and view the amount of posts created by each user.

    * Only staff users can view the user list.
    """

    model = User
    context_object_name = 'users'
    template_name = 'core/user_list.html'
