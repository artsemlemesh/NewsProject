# Generated by Django 4.2.3 on 2023-11-05 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0003_alter_post_time_of_creation"),
    ]

    operations = [
        migrations.CreateModel(
            name="One",
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
                ("name", models.CharField(help_text="category name", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Two",
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
                ("name", models.CharField(max_length=100)),
                (
                    "kind",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="kinds",
                        to="application.one",
                        verbose_name="this is the help text",
                    ),
                ),
            ],
        ),
    ]
