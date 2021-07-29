from core.models import UserLoginActivity
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from ipware import get_client_ip


@receiver(post_save, sender=User)
def create_user_login_activity(sender, instance, created, **kwargs):
    """
    Automatically create a 'UserLoginActivity' instance associated to the 'User' when a new 'User' instance is created.
    """

    if created:
        UserLoginActivity.objects.create(user=instance)


@receiver(user_logged_in)
def alert_different_ip(sender, request, user, **kwargs):
    """
    Automatically store the last IP that accessed the platform for a certain user,
    in order to show a warning message when this is different from the previous one.
    """

    ip, is_routable = get_client_ip(request)
    user_activity = UserLoginActivity.objects.get(user=user)

    if user_activity.last_login_IP == ip or user_activity.last_login_IP is None:
        user_activity.alert = False
    else:
        user_activity.alert = True
    user_activity.last_login_IP = ip
    user_activity.save()
