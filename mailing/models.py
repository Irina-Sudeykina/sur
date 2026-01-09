import datetime

from django.db import models
from django.utils.timezone import now as timezone_now
from django.core.exceptions import ValidationError

class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name="Ф.И.О.", help_text="Введите Ф.И.О.")
    comment = models.TextField(
        blank=True, null=True, verbose_name="Комментарий", help_text="Введите комментарий"
    )

    class Meta:
        verbose_name = "Получатель рассылки"
        verbose_name_plural = "Получатели рассылки"
        ordering = [
            "name",
            "email",
        ]

    def __str__(self):
        return f"{self.email} - {self.name}"


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема письма", help_text="Введите тему письма")
    body = models.TextField(
        blank=True, null=True, verbose_name="Тело письма", help_text="Введите текст письма"
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("created", "Создана"),
        ("started", "Запущена"),
        ("completed", "Завершена"),
    ]

    start_time = models.DateTimeField(verbose_name="Дата и время начала отправки")
    end_time = models.DateTimeField(verbose_name="Дата и время окончания отправки")
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Сообщение",
    )
    recipients = models.ManyToManyField(
        Recipient,
        related_name="mailings",
        verbose_name="Получатели",
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="created",
        editable=False,
        verbose_name="Статус",
    )

    class Meta:
            verbose_name = "Рассылка"
            verbose_name_plural = "Рассылки"
            ordering = [
                "start_time",
                "status",
            ]

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("Время начала должно быть раньше времени окончания.")
        
        current_time = timezone_now()
        if self.start_time <= current_time:
            raise ValidationError("Время начала не может быть в прошлом.")

    def update_status(self):
        """
        Динамическое обновление статуса рассылки.
        """
        current_time = timezone_now()
        if current_time < self.start_time:
            new_status = "created"
        elif self.start_time <= current_time <= self.end_time:
            new_status = "started"
        else:
            new_status = "completed"
            
        if self.status != new_status:
            self.status = new_status
            self.save(update_fields=["status"])

    def save(self, *args, **kwargs):
        """Автоматическое обновление статуса при сохранении."""
        super().save(*args, **kwargs)
        self.update_status()  # Обновляем статус сразу после сохранения

    def __str__(self):
        return f"Рассылка {self.id}: {self.message.subject}"


class AttemptLog(models.Model):
    attempt_time = models.DateTimeField(default=timezone_now, verbose_name="Дата и время попытки")
    status = models.CharField(max_length=20, choices=[
        ('successful', 'Успешно'),
        ('unsuccessful', 'Не успешно'),
    ], verbose_name="Статус")
    server_response = models.TextField(blank=True, verbose_name="Ответ почтового сервера")
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE, verbose_name="Рассылка")

    class Meta:
            verbose_name = "Попытка рассылки"
            verbose_name_plural = "Попытки рассылки"
            ordering = [
                "attempt_time",
                "status",
            ]

    def __str__(self):
        return f'{self.attempt_time}: {self.status}'
