# Generated by Django 4.1.7 on 2023-08-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0009_movie_director_alter_movie_budget_alter_movie_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="director_email",
            field=models.EmailField(default="sugar_daddy@gmail.com", max_length=254),
        ),
    ]
