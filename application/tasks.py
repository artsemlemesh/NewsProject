from django.core.mail import send_mail


def send_mails():
    print('hello from Mike')


def send_email_task():
    send_mail(
        subject='This subject is from django',
        message='This message is from DJANGO',
        from_email='artsemlemesh@mail.ru',
        recipient_list=['artsemlemesh@yandex.by']
    )