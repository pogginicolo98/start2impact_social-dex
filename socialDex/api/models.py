from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
