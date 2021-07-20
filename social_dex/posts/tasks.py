from celery import shared_task
from datetime import date, timedelta
from django.contrib.auth.models import User
from posts.models import PostReport
from redis import Redis


@shared_task
def users_activity_report():
    """
    Collects previous day reports from Redis then
    aggregates them into a single report on Sqlite.

    Data on Redis:
    - list: dd-mm-YYYY[HH:MM:SS - Mario has created a new post, HH:MM:SS - Luigi has retrieved a posts list, ...]

    Data on Sqlite:
    - date: YYYY-mm-dd
    - report: Mario has retrieved a posts list 0 times and has created a new post 1 times.
              Luigi has retrieved a posts list 1 times and has created a new post 0 times.
    """

    redis_reports = {}
    sqlite_report = ''
    yesterday = date.today() - timedelta(days=1)
    list_name = yesterday.strftime('%d/%m/%Y')
    redis_client = Redis('localhost', port=6379)
    redis_key = redis_client.lrange(list_name, 0, -1)

    # Collects previous day reports from Redis
    for redis_value in redis_key:
        record = redis_value.decode()  # Ex. 'HH:MM:SS - Mario has created a new post'
        user = record.split(' ')[2]
        if user not in redis_reports:  # Ex. {'Mario': {'post-list': 0, 'new-post': 1}, 'Luigi': {'post-list': 1, 'new-post': 0}}
            redis_reports[user] = {
                'post-list': 0,
                'new-post': 0,
            }
        if 'has retrieved a posts list' in record:
            redis_reports[user]['post-list'] += 1
        elif 'has created a new post' in record:
            redis_reports[user]['new-post'] += 1

    # Aggregates reports into a single report in order to store it on Sqlite.
    redis_users = list(redis_reports)
    for redis_user in redis_users:
        user = User.objects.get(username=redis_user)
        number_post_list = redis_reports[redis_user]['post-list']
        number_new_post = redis_reports[redis_user]['new-post']
        sqlite_report += f"{user.username} has retrieved a posts list {number_post_list} times and has created a new post {number_new_post} times.\n"
    PostReport.objects.create(date=yesterday, report=sqlite_report)
