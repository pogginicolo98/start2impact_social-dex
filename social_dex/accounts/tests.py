from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class SignUpViewTests(TestCase):
    """
    signup_view test case.
    View function that provides `create()` action.

    Tests:
    - test_signup_view_url_by_name(): Test url by name.
    """

    url = reverse('signup_view')

    def test_signup_view_url_by_name(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
