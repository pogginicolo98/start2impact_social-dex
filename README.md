# Start2Impact Python exercise: Blockchain bulletin board

Description:
Exercise to practice with Django, Django REST Framework and Ropsten network.
Web-app for an online bulletin board that writes posts on the Ropesten network blockchain.
Only authenticated users can retrieve a list of all posts or create a new one.
When a user creates a new post, it is automatically written to the blockchain in the form of a hash.
With the original message and the transaction id it is possible to verify the existence of the message on the Ropsten network blockchain.
The web-app provide two API endpoints:
1) Retrieve a list of all posts.
2) Create a new post.

Core files:
- [models.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/models.py)
- [serializers.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/serializers.py)
- [signals.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/signals.py)
- [tests.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/tests.py)
- [utils.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/utils.py)
- [views.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/views.py)
- [wallet.py](https://github.com/pogginicolo98/start2impact_social-dex/blob/master/socialDex/api/wallet.py)
