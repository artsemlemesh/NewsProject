# Generated by Django 4.2.3 on 2023-09-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_post_time_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_of_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]