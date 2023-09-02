from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        to='NewsCategory',
        on_delete=models.CASCADE,
        related_name='news',
    )


    # def send_email_notification(self):
    #     for subscriber in self.subscribers.all():
    #         email = subscriber.email


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # added subscribers filed
    # subscribers = models.ManyToManyField(User, blank=True, related_name='categories')

    def __str__(self):
        return self.name.title()

