from django.db import models


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
