# Generated by Django 4.1.4 on 2023-12-12 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("newapp", "0004_alter_contact_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="datetime",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 11, 19, 40, 40, 191356)
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=100),
        ),
    ]