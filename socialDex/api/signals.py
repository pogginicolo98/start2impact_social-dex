from api.models import Post
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch.dispatcher import Signal
from redis import Redis

# Creating custom signal for views: posts() and new_post()
posts_api_view_called = Signal(providing_args=['request'])
new_post_api_view_called = Signal(providing_args=['request'])


@receiver(post_save, sender=Post)
def auto_write_on_chain(sender, instance, created, **kwargs):
    """
    Automatically write on chain the new 'Post' created.
    When a model is created (in this case Post) Django automatically create a signal to notify this event (post_save),
    the wrapper 'receiver()' catch this signal and this function create a new instance based on this event.
    """

    if created:
        instance.write_on_chain()


def posts_api_view_called_handler(sender, request, **kwargs):
    """
    Automatically register on Redis the call of the view function 'posts()' by the user.

    Data format on Redis:
    - List
    - Key: dd-mm-YYYY
    - Values: HH:MM:SS - user has retrieved a posts list
    """

    redis_client = Redis('localhost', port=6379)
    redis_client.lpush(
        datetime.now().strftime('%d/%m/%Y'),
        f"{datetime.now().strftime('%H:%M:%S')} - {request.user} has retrieved a posts list"
    )


def new_post_api_view_handler(sender, request, **kwargs):
    """
    Automatically register on Redis the call of the view function 'new_post()' by the user.

    Data format on Redis:
    - List
    - Key: dd-mm-YYYY
    - Values: HH:MM:SS - user has created a new post
    """

    redis_client = Redis('localhost', port=6379)
    redis_client.lpush(
        datetime.now().strftime('%d/%m/%Y'),
        f"{datetime.now().strftime('%H:%M:%S')} - {request.user} has created a new post"
    )


# Connecting custom signals for views: posts() and new_post()
posts_api_view_called.connect(posts_api_view_called_handler)
new_post_api_view_called.connect(new_post_api_view_handler)
