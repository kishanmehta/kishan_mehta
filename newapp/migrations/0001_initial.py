# Generated by Django 4.1.4 on 2023-12-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("notes", models.CharField(max_length=300)),
                ("time", models.TimeField()),
            ],
        ),
    ]
