# Generated by Django 4.1.7 on 2023-08-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0010_movie_director_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "director_email",
                    models.EmailField(default="sugar_daddy@gmail.com", max_length=254),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="movie",
            name="director",
        ),
        migrations.RemoveField(
            model_name="movie",
            name="director_email",
        ),
    ]
