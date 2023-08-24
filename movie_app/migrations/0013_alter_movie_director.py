# Generated by Django 4.1.7 on 2023-08-24 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("movie_app", "0012_movie_director"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="movie_app.director",
            ),
        ),
    ]
