# Generated by Django 4.2.3 on 2023-11-05 07:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0004_one_two"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="two",
            name="kind",
        ),
        migrations.DeleteModel(
            name="One",
        ),
        migrations.DeleteModel(
            name="Two",
        ),
    ]