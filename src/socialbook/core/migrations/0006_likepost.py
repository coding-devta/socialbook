# Generated by Django 4.1.1 on 2022-10-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_delete_likepost"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
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
                ("post_id", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=200)),
            ],
        ),
    ]
