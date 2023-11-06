# Generated by Django 4.2.3 on 2023-11-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0005_remove_two_kind_delete_one_delete_two"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content_of_article_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="content_of_article_ru",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title_en",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title_ru",
            field=models.CharField(max_length=255, null=True),
        ),
    ]