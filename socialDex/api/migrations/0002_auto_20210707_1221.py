# Generated by Django 3.2.4 on 2021-07-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hash',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tx_id',
            field=models.CharField(default=None, max_length=66, null=True),
        ),
    ]
