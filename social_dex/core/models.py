from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    """ Base Model class for explicit objects attribute to avoid 'Unresolved attribute reference...' """

    objects = models.Manager()

    class Meta:
        abstract = True


class UserLoginActivity(BaseModel):
    """
    Users login activity tacker.
    Extension of the 'User' model.
    A report that tracks the last IP used by each user.

    fields:
    - user: Each 'User' corresponds to one and only one 'UserLoginActivity'.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_login_IP = models.GenericIPAddressField(blank=True, null=True)
    alert = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
