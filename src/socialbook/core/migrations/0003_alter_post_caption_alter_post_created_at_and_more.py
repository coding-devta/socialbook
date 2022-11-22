# Generated by Django 4.1.1 on 2022-09-26 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post", name="caption", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="post", name="no_likes", field=models.IntegerField(default=0),
        ),
    ]
