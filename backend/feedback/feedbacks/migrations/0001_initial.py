# Generated by Django 4.1.3 on 2022-11-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("feedback", models.TextField(max_length=1000)),
                ("email", models.EmailField(default=None, max_length=256, null=True)),
            ],
        ),
    ]
