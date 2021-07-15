from api.utils import send_transaction
from django.contrib.auth.models import User
from django.db import models
import hashlib


class BaseModel(models.Model):
    """ Base Model class for explicit objects attribute to avoid 'Unresolved attribute reference...' """

    objects = models.Manager()

    class Meta:
        abstract = True


class Post(BaseModel):
    """
    A post that can write messages on the blockchain.
    To write the message on chain, first it calculate the hash of the 'content' then added to the 'data' field of the transaction.
    In that way, by comparing the hash calculated by the message and the one present on the blockchain
    referred to the transaction with id = 'tx_id', it is possible to verify the integrity and presence of the message on the blockchain.

    Actual network: Ropsten.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    hash = models.CharField(max_length=64, blank=True, null=True)
    tx_id = models.CharField(max_length=66, blank=True, null=True)  # max_length: see the structure of the transaction id of the network used.

    def __str__(self):
        return f"{self.user} | {self.datetime}"

    def write_on_chain(self):
        # Automatically called when a new 'Post' is created (see api/signals.py)

        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.tx_id = send_transaction(self.hash)
        self.save()
