from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class HomepageTests(TestCase):
    """
    HomepageView tests.

    tests:
    - test_homepage_url_by_name(): Test url by name.
    """

    def test_homepage_url_by_name(self):
        url = reverse('homepage-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
