# Start2Impact Django&Redis project: Blockchain bulletin board

Online bulletin board that writes posts on the Ropesten network blockchain.
The web-app provides a user interface and API endpoints with the following features:

User interface
1) User registration and authentication.
2) Write a new post and view all posts written by users.
3) User profile.
4) User list and statistics (Administrators only).

API endpoints
1) /api/rest-auth/registration/ : User registration via token.
2) /api/rest-auth/login/ : Authentication via token.
3) /api/new-post/ : Create a new post.
4) /api/posts/ : Retrieve all posts written by users.
5) /api/posts/?search=word_to_search_for : Retrieve the number of posts that contain a certain word.
6) /api/posts/latest/ : Retrieve all posts published in the last hour.

The web-app also integrates a filter for posts containing the word 'hack', performs a daily report logging the use of endpoints by users and keeps track of the last IP with which users logged in to notify if it is different from the previous one.

Live demo: [SocialDex](http://13.36.123.111/)

<hr>

Frameworks and technologies used:

Frameworks
- [Django](https://docs.djangoproject.com/en/3.2/) - Main back-end
- [Django REST Framework](https://www.django-rest-framework.org/) - APIs
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Main front-end

Databases
- [SQLite](https://sqlite.org/docs.html) - Main storage
- [Redis](https://redis.io/documentation) - Daily logs

Technologies
- [Celery](https://docs.celeryproject.org/en/stable/#) - Scheduled tasks
