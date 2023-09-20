import datetime
import time

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


from .models import Category, Post

from celery import shared_task


# @shared_task
# def hello():
#     time.sleep(10)
#     print('hello, World')
#
#
# @shared_task
# def printer(N):
#     for i in range(N):
#         time.sleep(1)
#         print(i+1)


@shared_task
def week_notifications():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_of_creation__gte=last_week)

    categories = posts.value_list('category__category')

    subscribers = set(Category.objects.filter(categories__in=categories).value_list('subscribers__email', flat=True))

    html_content = render_to_string('account/email/weekly_post.html',
                                    {
                                        'link': settings.SITE_URL,
                                        'posts': posts
                                    })
    msg = EmailMultiAlternatives(
        subject='weekly articles',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


#celery --app=mcdonalds worker -l INFO

# celery --app=NewsProject worker -l INFO -B
# celery --app=mcdonalds worker -l INFO

# def send_mails():
#     print('hello from Mike')
#
#
# def send_email_task():
#     send_mail(
#         subject='This subject is from django',
#         message='This message is from DJANGO',
#         from_email='artsemlemesh@mail.ru',
#         recipient_list=['artsemlemesh@yandex.by']
#     )