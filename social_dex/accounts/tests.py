from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class SignUpViewTests(TestCase):
    """
    Signup_view test case.
    View function that provides `create()` action.

    A class that perform the following tests:
    1 - Url by name
    """

    def test_signup_view_url_by_name(self):
        url = reverse('signup_view')
        response = self.client.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)
