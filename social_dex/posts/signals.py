from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Post


@receiver(post_save, sender=Post)
def auto_write_on_chain(sender, instance, created, **kwargs):
    """
    Automatically write on chain the new 'Post' created.
    When a model is created (in this case Post) Django automatically create a signal to notify this event (post_save),
    the wrapper 'receiver()' catch this signal and this function create a new instance based on this event.
    """

    if created:
        instance.write_on_chain()
