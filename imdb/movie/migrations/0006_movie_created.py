# Generated by Django 2.2.5 on 2020-04-16 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 5, 35, 22, 876056, tzinfo=utc)),
        ),
    ]