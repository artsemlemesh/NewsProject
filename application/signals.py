from django.core.mail import EmailMultiAlternatives, mail_managers
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from django.conf import settings
from .models import PostCategory


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
        from_email= 'Artsemlemesh1@yandex.com',
        to= subscribers
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    subject = f'{instance.title} {instance.categories}'
    # else:
    #     subject = f'Something changed for {instance.post} {instance.category}'

    mail_managers(
        subject= subject,
        message= instance.categories

    )
m2m_changed.connect(notify_about_new_post, sender=PostCategory)