# Generated by Django 4.2.1 on 2023-05-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiktok', '0010_alter_movie_createdtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]