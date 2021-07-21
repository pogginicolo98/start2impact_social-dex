import json
from datetime import timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from posts.models import Post


class RESTAuthTestCase(APITestCase):
    """
    Django REST Auth configuration test case.

    tests:
    - test_authentication(): Log in with a user via Django REST Auth APIs.
    - test_registration(): Register a new user via Django REST Auth APIs.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='Change_me_123!')

    def test_authentication(self):
        credentials = {
            'username': 'testcase',
            'password': 'Change_me_123!'
        }
        response = self.client.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
        json_response = json.loads(response.content)
        token = f"Token {json_response['key']}"
        headers = {'Authorization': token}
        response = self.client.get('http://127.0.0.1:8000/post/api/posts/', headers=headers)
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


class PostsAPITestCase(APITestCase):
    """
    posts() view function test case.
    View function that provides `list()` action.

    tests:
    - test_post_list_not_authenticated(): Test 'list()' action by an unauthenticated user.
    - test_post_list_authenticated(): Test 'list()' action by an authenticated user.
    """

    list_url = reverse('post-list')
    create_url = reverse('new-post')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='Change_me_123!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_post_list_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NewPostAPITestCase(APITestCase):
    """
    new_post() view function test case.
    View function that provides `create()` action.

    tests:
    - test_post_create_not_authenticated(): Test 'create()' action by an unauthenticated user.
    - test_post_create_authenticated(): Test 'create()' action by an authenticated user.
    """

    create_url = reverse('new-post')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='Change_me_123!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_post_create_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_authenticated(self):
        data = {
            'content': 'Test'
        }
        response = self.client.post(self.create_url, data=data)
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['user'], 'testcase')
        self.assertEqual(json_response['content'], 'Test')


class PostListCreateViewTestCase(TestCase):
    """
    PostListCreateView test case.
    Generic CreateVIew that provide 'list()' and 'create()' actions.

    tests:
    - test_post_list_create_url_by_name_not_authenticated(): Test url by name by an unauthenticated user.
    - test_post_list_create_url_by_name_authenticated(): Test url by name by an authenticated user.
    - test_post_list_create_new_post_not_authenticated(): Test 'post()' action by an unauthenticated user.
    - test_post_list_create_new_post_authenticated(): Test 'post()' action by an authenticated user.
    """

    url = reverse('post-list-create')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='Change_me_123!')

    def test_post_list_create_url_by_name_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('login') + '?next=' + self.url)

    def test_post_list_create_url_by_name_authenticated(self):
        self.client.login(username='testcase', password='Change_me_123!')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list_create_new_post_not_authenticated(self):
        data = {'content': 'Test message'}
        response = self.client.post(self.url, data=data)
        posts = Post.objects.all().count()
        self.assertEqual(posts, 0)
        self.assertRedirects(response, reverse('login') + '?next=' + self.url)

    def test_post_list_create_new_post_authenticated(self):
        data = {'content': 'Test message'}
        self.client.login(username='testcase', password='Change_me_123!')
        response = self.client.post(self.url, data=data)
        post = Post.objects.get(pk=1)
        self.assertEqual(post.content, data['content'])
        self.assertEqual(post.user.username, 'testcase')


class PostLatestListAPIViewTestCase(APITestCase):
    """
    PostLatestListAPIView test case.
    Generic APIView that provides `list()` action.

    tests:
    - test_status_list(): Test 'list()' action.
    """

    create_url = reverse('new-post')
    list_url = reverse('post-latest')

    def setUp(self):
        self.user = User.objects.create_user(username='testcase', password='Change_me_123!')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.client.post(self.create_url, data={'content': 'more than 1 hours ago'})
        self.client.post(self.create_url, data={'content': 'less than 1 hour ago'})

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_post_latest_list(self):
        two_hour_ago = timezone.now() - timedelta(hours=2)
        post = Post.objects.get(pk=1)
        post.datetime = two_hour_ago
        post.save()
        response = self.client.get(self.list_url)
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['content'], 'less than 1 hour ago')
