# Generated by Django 3.2.4 on 2021-07-15 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_post_post_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_message',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_info',
        ),
    ]
