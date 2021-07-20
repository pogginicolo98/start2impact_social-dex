import json
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RESTAuthTestCase(APITestCase):
    """
    Django REST Auth configuration test case.

    tests:
    - test_authentication(): Log in with a user via Django REST Auth APIs.
    - test_registration(): Register a new user via Django REST Auth APIs.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='testcase1', password='Change_me_123!')

    def test_authentication(self):
        credentials = {
            'username': 'testcase1',
            'password': 'Change_me_123!'
        }
        response = self.client.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
        json_response = json.loads(response.content)
        token = f"Token {json_response['key']}"
        headers = {'Authorization': token}
        response = self.client.get('http://127.0.0.1:8000/api/posts/', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_registration(self):
        data = {
            'username': 'testcase2',
            'email': 'testcase@local.app',
            'password1': 'Change_me_123!',
            'password2': 'Change_me_123!',
        }
        response = self.client.post('/api/rest-auth/registration/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PostsTestCase(APITestCase):
    """
    posts() view function test case.
    view function that provides `list()` action.

    tests:
    - test_post_list_not_authenticated(): Test 'list()' action by an unauthenticated user.
    - test_post_list_authenticated(): Test 'list()' action by an authenticated user.
    """

    list_url = reverse('post-list')
    create_url = reverse('new-post')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase1', password='Change_me_123!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_post_list_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)  # Ex. URL: http://127.0.0.1/api/posts/
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_list_authenticated(self):
        response = self.client.get(self.list_url)  # Ex. URL: http://127.0.0.1/api/posts/
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NewPostTestCase(APITestCase):
    """
    new_post() view function test case.
    view function that provides `create()` action.

    tests:
    - test_post_create_not_authenticated(): Test 'create()' action by an unauthenticated user.
    - test_post_create_authenticated(): Test 'create()' action by an authenticated user.
    """

    create_url = reverse('new-post')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase1', password='Change_me_123!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_post_create_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.create_url)  # Ex. URL: http://127.0.0.1/api/new-post/
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_authenticated(self):
        data = {
            'content': 'Test'
        }
        response = self.client.post(self.create_url, data=data)  # Ex. URL: http://127.0.0.1/api/new-post/
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['user'], 'testcase1')
        self.assertEqual(json_response['content'], 'Test')


class HomepageTests(TestCase):
    """
    HomepageView tests.

    A class that perform the following tests:
    1 - Url by name
    """

    def test_homepage_url_by_name(self):
        url = reverse('homepage-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostListCreateViewTests(TestCase):
    """
    PostListCreateView tests.

    A class that perform the following tests:
    1 - Url by name
    """

    def setUp(self):
        self.user = User.objects.create_user(username='testcase1', password='Change_me_123!')

    def test_redirects_to_test_page_on_not_authenticated(self):
        url = reverse('post-list-create')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login') + '?next=' + url)

    def test_redirects_to_test_page_on_authenticated(self):
        self.client.login(username='testcase1', password='Change_me_123!')
        url = reverse('post-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
