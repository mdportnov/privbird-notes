# Generated by Django 4.1.3 on 2022-11-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("real_content", models.TextField(max_length=40000, null=True)),
                (
                    "real_password",
                    models.CharField(default=None, max_length=100, null=True),
                ),
                ("real_notification", models.BooleanField(default=False)),
                (
                    "fake_content",
                    models.TextField(default=None, max_length=40000, null=True),
                ),
                (
                    "fake_password",
                    models.TextField(default=None, max_length=100, null=True),
                ),
                ("fake_notification", models.BooleanField(default=None, null=True)),
                ("expires", models.DateTimeField()),
                ("email", models.EmailField(default=None, max_length=256, null=True)),
                ("salt", models.CharField(default=None, max_length=32, null=True)),
                ("slug", models.SlugField(max_length=12, unique=True)),
            ],
        ),
    ]
