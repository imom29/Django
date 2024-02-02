# Generated by Django 5.0.1 on 2024-02-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StreamPlatform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
                ("website", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Watchlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("storyline", models.CharField(max_length=200)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Movie",
        ),
    ]
