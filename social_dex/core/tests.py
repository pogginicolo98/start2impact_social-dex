from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class UserListViewTestCase(TestCase):
    """
    UserListView test case.
    Generic ListView that provide 'list()' action.

    tests:
    - test_user_list_url_by_name_not_authenticated(): Test url by name by an unauthenticated user.
    - test_user_list_url_by_name_random_user(): Test url by name by a non-staff user.
    - test_user_list_url_by_name_authenticated(): Test url by name by a staff user.
    """

    url = reverse('user-list')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase1', password='Change_me_123!')
        self.user = User.objects.create_superuser(username='testcase2', password='Change_me_123!')

    def test_user_list_url_by_name_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('login') + '?next=' + self.url)

    def test_user_list_url_by_name_random_user(self):
        self.client.login(username='testcase1', password='Change_me_123!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_list_url_by_name_authenticated(self):
        self.client.login(username='testcase2', password='Change_me_123!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserDetailViewTestCase(TestCase):
    """
    UserDetailView test case.
    Generic DetailView that provide 'retrieve()' action.

    tests:
    - test_user_detail_url_by_name(): Test url by name and 'retrieve()' action.
    """

    url = reverse('user-detail', kwargs={'pk': 1})

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='Change_me_123!')

    def test_user_detail_url_by_name(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
