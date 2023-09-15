from django.apps import AppConfig

class ApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'application'

    def ready(self):
        from . import signals
        #
        # from .tasks import send_mails, send_email_task
        # from .scheduler import appointment_scheduler
        # print('started')
        # appointment_scheduler.add_job(
        #     id='mail send',
        #     func=send_email_task,
        #     trigger='interval',
        #     seconds=10,
        # )
        # appointment_scheduler.start()