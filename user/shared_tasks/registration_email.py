from celery import shared_task, Celery
from django.conf import settings

@shared_task(queue=settings.CELERY_QUEUE)
def send_registration_email(pattern,user):
    print("Sending registration email to the user")
    return None
