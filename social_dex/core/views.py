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
    ???
    """

    model = User
    template_name = 'core/user_list.html'
    context_object_name = 'users'
