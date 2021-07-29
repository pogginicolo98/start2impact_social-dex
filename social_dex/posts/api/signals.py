from datetime import datetime
from django.dispatch.dispatcher import Signal
from redis import Redis

# Creating custom signal for views: posts() and new_post()
posts_api_view_called = Signal(providing_args=['request'])
new_post_api_view_called = Signal(providing_args=['request'])


def posts_api_view_called_handler(sender, request, **kwargs):
    """
    Log on Redis the user's activity when accessing the view function 'posts()'.

    Data format on Redis:
    - Type: List.
    - Key: dd-mm-YYYY.
    - Values: HH:MM:SS - user has retrieved a posts list.
    """

    redis_client = Redis('localhost', port=6379)
    key = datetime.now().strftime('%d/%m/%Y')
    value = f"{datetime.now().strftime('%H:%M:%S')} - {request.user} has retrieved a posts list"
    redis_client.lpush(key, value)


def new_post_api_view_handler(sender, request, **kwargs):
    """
    Log on Redis the user's activity when accessing the view function 'new_post()'.

    Data format on Redis:
    - Type: List.
    - Key: dd-mm-YYYY.
    - Values: HH:MM:SS - user has created a new post.
    """

    redis_client = Redis('localhost', port=6379)
    key = datetime.now().strftime('%d/%m/%Y')
    value = f"{datetime.now().strftime('%H:%M:%S')} - {request.user} has created a new post"
    redis_client.lpush(key, value)


# Connecting custom signals for views: posts() and new_post()
posts_api_view_called.connect(posts_api_view_called_handler)
new_post_api_view_called.connect(new_post_api_view_handler)
