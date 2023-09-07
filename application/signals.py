from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_managers
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from django.conf import settings
from .models import PostCategory, Post


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers: list = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]
        print(subscribers)

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)


# @receiver(m2m_changed, sender=Post.categories.through)
# def notify_subscribers(instance, action, *args, **kwargs):
#     users_emails = []
#     if action == 'post_add':
#         users_emails = [
#             user.email
#             for categories in instance.categories.all()
#             for user in categories.subscribers.all()
#         ]
#     for email in users_emails:
#         user = User.objects.get(email=email)
#         html_content = render_to_string('post_created_email.html', {'post_mail': instance}, )
#
#         subject = f'Hello, {user.username}. New article arrived'
#         from_email = f'{settings.DEFAULT_FROM_EMAIL}'
#         send_notifications(subject, from_email, email, html_content)










def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/articles/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email= settings.DEFAULT_FROM_EMAIL,
        to= subscribers
    )
    print(subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()








@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    subject = f'{instance.title} {instance.categories}'
    ## else:
    ##     subject = f'Something changed for {instance.post} {instance.category}'

    mail_managers(
        subject= subject,
        message= instance.categories

    )
m2m_changed.connect(notify_about_new_post, sender=PostCategory)