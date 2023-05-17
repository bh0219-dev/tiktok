# Generated by Django 4.2.1 on 2023-05-15 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0005_alter_movie_createdtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='createdtime',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2023, 5, 15, 7, 40, 10, 38641), null=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='moviesrc',
            field=models.FileField(upload_to='movies/'),
        ),
    ]