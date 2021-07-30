# Start2Impact Django&Redis project: Blockchain bulletin board

Online bulletin board that writes posts on the Ropesten network blockchain.
The web-app provides a user interface and API endpoints with the following features:

User interface
1) User registration and authentication.
2) Write a new post and view all posts written by users.
3) User profile.
4) User list and statistics (Administrators only).

API endpoints
1) User registration and authentication via token.
2) Create a new post.
3) Retrieve all posts written by users.
4) Retrieve the number of posts that contain a certain word.
5) Retrieve all posts published in the last hour.

The web-app also integrates a filter for posts containing the word 'hack', performs a daily report logging the use of endpoints by users and keeps track of the last IP with which users logged in to notify if it is different from the previous one.

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
