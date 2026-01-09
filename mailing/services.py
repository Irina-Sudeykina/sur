from django.core.mail import send_mail
from django.utils.timezone import now as timezone_now
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .models import AttemptLog
from django.conf import settings


def send_messages_by_request(mailing):
    current_time = timezone_now()
    if mailing.start_time <= current_time <= mailing.end_time:
        for recipient in mailing.recipients.all():
            try:
                response = send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[recipient.email],
                    fail_silently=False
                )
                
                if response > 0:
                    log = AttemptLog.objects.create(
                        status='successful',
                        mailing=mailing,
                        server_response=f'Письмо доставлено ({recipient.email} - {response})'
                    )
                else:
                    log = AttemptLog.objects.create(
                        status='unsuccessful',
                        mailing=mailing,
                        server_response='Ошибка отправки!'
                    )
                    
            except Exception as e:
                log = AttemptLog.objects.create(
                    status='unsuccessful',
                    mailing=mailing,
                    server_response=str(e)
                )
    else:
        return False  # Возвращаем False, если рассылка невозможна
