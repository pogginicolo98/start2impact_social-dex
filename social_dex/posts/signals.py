from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Post


@receiver(post_save, sender=Post)
def auto_write_on_chain(sender, instance, created, **kwargs):
    """
    Write the 'Post' on chain when it is created.
    When a model is created (in this case Post) Django automatically create a signal to notify this event (post_save),
    the wrapper 'receiver()' catch this signal and this function create a new instance based on this event.

    * Comment this function during tests, multiple transactions may be generated and a GAS error may occur.
    """

    if created:
        instance.write_on_chain()
